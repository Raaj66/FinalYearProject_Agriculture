from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from tablib import Dataset
from rapidconnect import RapidConnect  # to use a rapid api
import pprint  # pretty print a json
import requests  # access apis
import datetime  # get current date and time
import statistics  # calculate mean

count = 0


# =======================================FOR WORK USING THE API OF WEATHER AND SOIL DETAILS=====================================


# to get the current temperature and weather information
def api_for_weather(place):
    result = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + place + '&appid=486d45a8672282f2149439e3fc7bfe40')
    data = result.json()
    return data


def ave(l):
    return sum(l) / float(len(l))


def Crop_Fertilizers_Final(predii, input_Crop):
    print("input crop", input_Crop)
    data = 0
    ggg = []
    print("Predicted", predii)
    if (input_Crop == "Tea"):
        ggg = predii[0:4]  # tea 0.9
        data = ave(ggg)

    if (input_Crop == "Oilseeds"):
        print("Oilseeds man")
        ggg = predii[5:7]
        data = ave(ggg)

    if (input_Crop == "Barley"):
        print("Barley man")
        ggg = predii[8:10]
        data = ave(ggg)

    if (input_Crop == "Sugercane"):
        print("Sugercane man")
        ggg = predii[11:16]
        data = ave(ggg)

    if (input_Crop == "Millets"):
        print("Millets man")
        ggg = predii[17:21]
        data = ave(ggg)

    if (input_Crop == "Maize"):
        print("Maize man")
        ggg = predii[22:24]
        data = ave(ggg)

    if (input_Crop == "Rice"):
        print("Rice man")
        ggg = predii[25:30]
        data = ave(ggg)

    if (input_Crop == "Groundnut"):
        print("Groundnut man")
        ggg = predii[31:41]
        data = ave(ggg)

    if (input_Crop == "Bajra"):
        print("Bajra man")
        ggg = predii[42:47]
        data = ave(ggg)

    if (input_Crop == "Sorghum"):
        print("Sorghum man")
        ggg = predii[48:54]
        data = ave(ggg)

    if (input_Crop == "Wheat"):
        print("Wheat man")
        ggg = predii[55:70]
        data = ave(ggg)

    ###We should add remaining crops

    print("data", data)
    return data


def Fertilizers_Regrs(input):
    import pandas as pd
    import numpy as np
    import sklearn
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    dataset = pd.read_excel('cultivo_main/Agri_Fertilizers_Used.xls')

    dataset = dataset.values

    Y = dataset[0:, 3:4]
    X = dataset[:, [1, 3, 4, 5]]

    X = list(X)
    print(X)

    X_trian, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

    model = LinearRegression()
    model.fit(X_trian, Y_train)

    X_test = list(X_test)
    # print(X_test)
    df = pd.DataFrame(X_test, columns=["ID", "A", "B", "C"])
    df.sort_values('ID')
    # print(df)
    final_df = df.sort_values(by=['ID'], ascending=False)
    print("final df", final_df)

    final_df = np.array(final_df)
    predict = model.predict(final_df)
    print("Final Predict", predict)
    predict = list(predict)

    Predicted_Mean_Ferti_reci = Crop_Fertilizers_Final(predict, input)
    return Predicted_Mean_Ferti_reci


def api_for_weather_2(lat, longi):
    result = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(
        longi) + '&appid=486d45a8672282f2149439e3fc7bfe40')

    data = result.json()

    return data


def calculate_coord(data):
    try:

        coord = [data['coord']['lat'], data['coord']['lon']]
        return coord
    except Exception as e:
        print('coord returned method value', e)


# to get the information about the soil of the region or district

def get_soil_info(place, coord):
    now = datetime.datetime.now()
    print(str(coord[0]))
    print(coord[1])

    start_date = str(now.year) + '-' + str(now.month - 1) + '-' + str(now.day)
    end_date = str(now.year) + '-' + str(now.month + 1) + '-' + str(now.day)
    #    result=requests.get('https://api.weatherbit.io/v2.0/history/agweather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&start_date='+start_date+'&end_date='+end_date+'&key=283a77fe5cbe46718430e4d5418be6c1')
    result = requests.get('https://api.weatherbit.io/v2.0/forecast/agweather?lat=' + str(coord[0]) + '&lon=' + str(
        coord[1]) + '&key=fe1b65b62f9d4491b37bbdb7aef8acdd')
    data = result.json()
    return data


def cal_mean(data):
    mean_vals = []
    summ_vals_dict = {}
    keywords = ['bulk_soil_density', 'skin_temp_avg', 'precip', 'specific_humidity', 'pres_avg', 'soilt_0_10cm',
                'soilm_0_10cm', 'wind_10m_spd_avg']
    for k in keywords:
        summ = 0
        for i in range(0, 9):
            summ += data['data'][i][k]
        summ_vals_dict[k] = summ
    for key in summ_vals_dict:
        summ_vals_dict[key] = (summ_vals_dict[key]) / 9

    return summ_vals_dict


# daaa = api_for_geocon(place)
# return cal_mean(daaa)


def geocoding(place):
    coord = []
    result = requests.get(
        'https://api.opencagedata.com/geocode/v1/json?q=' + place + '&key=217e890a4fed4cc780a83c8cce2abf14')
    data = result.json()
    coord.append(data['results'][0]['geometry']['lat'])
    coord.append(data['results'][0]['geometry']['lng'])
    return coord


def print_temp_details(data):
    temp = precise((data['main']['temp'] - 273.15), 1)
    wind = precise((data['wind']['speed'] * 1.60934), 2)
    dire = precise((data['wind']['deg']), 2)

    values = {
        'temperature': str(temp),
        'latitude': str(data['coord']['lat']),
        'longitude': str(data['coord']['lon']),
        'humidity': str(data['main']['humidity']) + '%',
        'pressure': str(data['main']['pressure']) + 'hPa',
        'windspeed': str(wind) + 'km/h'
        # 'winddirection':str(dire)
        #    'visibility':str(data['visibility'])+' metres',
    }

    return values


def precise(data, point):
    if type(data) == dict:
        a = {}
        for i in data:
            if type(data[i]) == float:
                data[i] = round(data[i], point)
                a[i] = data[i]
            else:
                a[i] = data[i]
        return a
    if type(data) == float:
        return round(data, point)

    if type(data) == list:
        a = []
        for i in data:
            if type(i) == float:
                i = round(i, point)
                print(i)
                a.append(i)
            else:
                a.append(i)
        return a


def categorize(val1, val2):
    if val1 > val2:
        pp = (val2 / val1)
        return pp
    else:
        return 1


def finding_subs(p, crop1):
    d = {}
    for i in p.values():
        crop = i['crop']
        area = i['district']


        sec_datset = prod_area.objects.filter(crop=crop, district=area)
        third_datset = pred_three.objects.filter(crop=crop)

        if  sec_datset.count() != 0 and third_datset.count() != 0:
            sec_val = list(sec_datset.values())[0]
            val1 = sec_val['org_val']
            val2 = sec_val['pred_val']

            p1 = categorize(val1, val2)

            # handing the  Gross_Production_Value_current_million_US_dollar factor



            # handling the imports exports and production factors
            firr1 = list(third_datset.values())[0]

            val1_1 = firr1['exports']
            val2_2 = firr1['imports']
            val3_3 = firr1['production']

            val1_1_p = firr1['exports']
            val2_2_p = firr1['imports']
            val3_3_p = firr1['production']

            p3 = categorize(val1_1, val1_1_p)
            p4 = categorize(val2_2, val2_2_p)
            p5 = categorize(val3_3, val3_3_p)

            mean_final = (p1 + p3 + p4 + p5) / 4

            d[crop] = mean_final

    else:
        d[crop] = 'no db exist for the crop'

    e = {}
    for i in d:
        if type(d[i]) != str and i != crop1:
            e[i] = d[i]
    return e


# ==========================================MAIN DJANGO VIEWS=============================================


class TemplateView(generic.TemplateView):
    template_name = 'cultivo_main/login.html'


class TemplateView2(generic.TemplateView):
    template_name = 'cultivo_main/contact.html'


class TemplateView3(generic.TemplateView):
    template_name = 'cultivo_main/story.html'


class TemplateView4(generic.TemplateView):
    template_name = 'cultivo_main/services.html'


def Match_Lat_Lan():
    print("Its in Lan_langi")


def work(request):
    if request.method == 'POST':
        area = request.POST['area'].upper()  # here we are taken area
        crop = request.POST['crop'].capitalize()  # and perticuler crop
        if (prod_area.objects.filter(crop=crop, district=area)).count() >= 1:  ###if the crop and area fond

            data = api_for_weather(area)  ###gettting the weather details of the area
            print('1st api weather data is', data)

            # getting the json details of the atmosphere
            coord = geocoding(area)
            print("geocoding area", coord)
            print("this is the 2nd api just clarifyng the lang and lat")
            ##getting the same weather info

            if data['cod'] == 200:
                print("If its a Success of Response")
                data3 = api_for_weather_2(coord[0], coord[1])
                ###here we are taking langitude and latitude
                print("This is the  Third API which is using Lang and  Lat")
                print(data3)  ### Works as same like First APP
            else:
                return render(request, 'cultivo_main/error.html')

            temp_det = print_temp_details(data)

            print('tempo', temp_det)  # converting all the details into proper units for printing

            temp_det_2 = precise(temp_det, 1)  # filtering the objects rounding up

            first_datset = prod_area.objects.filter(crop=crop, district=area)

            third_datset = pred_three.objects.filter(crop=crop)

            # #gettting dictionaries out of the returned values

            fir_values = list(first_datset.values())[0]
            del fir_values['id']
            del fir_values['org_val']  ##here we are keeping only Pred_org means deleting org

            regression1 = fir_values
            print("Exact Pred Value of Crop", regression1['pred_val'])
            regre1 = regression1['pred_val']

            # making round figure

            third_values = list(third_datset.values())[0]
            del third_values['id']
            del third_values['crop']
            print('third_values', third_values)

            imports = third_values['imports']
            exports = third_values['exports']
            productions = third_values['production']

            regression3 = (imports + exports + productions) / 3
            print(type(regression3))

            print("regression3", regression3)

            agriResult = dict()

            ###Creating proper Dict to Configure in page

            agriResult['Pred_Value'] = regression1['pred_val']
            agriResult['import'] = imports
            agriResult['export'] = exports
            agriResult['production'] = productions
            agriResult[
                'Google'] = outer = "https://maps.google.com/maps?q=" + area + "&t=&z=13&ie=UTF8&iwloc=&output=embed"

            first_val = list(first_datset.values())[0]
            val1 = first_val['org_val']
            val2 = first_val['pred_val']
            p1 = categorize(val1, val2)
            print(type(p1))
            print('p1', p1)

            firr1 = list(third_datset.values())[0]
            val1_1 = firr1['exports']
            val2_2 = firr1['imports']
            val3_3 = firr1['production']

            a1 = categorize(val1_1, val2_2)
            a2 = categorize(val3_3, regression3)

            p3 = categorize(a1, a2)

            print("p3", p3)

            ########Dealing with Fertilizers#######

            cropdigit = []
            mean_final=0

            mean_final = (p1 + p3) / 2  ####Here we have to add our final mean
            print('mean final', mean_final)
            print(type(mean_final))
            mean_final = float(mean_final)
            mean_final=mean_final*100
            print("Mean", mean_final)


            print(Fertilizers_Regrs(crop))

            Regressed_Fertilizers = abs(Fertilizers_Regrs(crop))
            print("Regressed", Regressed_Fertilizers)



            hect = 0
            rate=0
            First_Out = float(regression1['pred_val'])

            print("first out", First_Out)
            if (0 <= Regressed_Fertilizers <= 35):
                print("Between 35")
                avevalu = 35 - Regressed_Fertilizers
                resu = First_Out - 1
                if (avevalu > 20 and resu > 1):
                    mean_final = mean_final + 2
                    rate=2
                if (avevalu > 20 and resu < 1):
                    mean_final = mean_final + 1
                    rate=1
            else:
                hect = Regressed_Fertilizers / 35
                print('Agri used hector', hect)
                resu = First_Out - 1

                if (resu > 1):
                    mean_final=mean_final+0.4
                    rate=4
                else:
                    print("prrrrr", resu * 10)
                    resu = abs(resu)
                    print("ddd", resu)
                    mean_final = mean_final - resu * 10
                    t=resu * 10
                    rate=0

            Weather_clime = temp_det['temperature']
            print("wheater", Weather_clime)
            Weather_clime = float(Weather_clime)
            if (22 <= Weather_clime <= 32):
                if (crop == "Rice"):
                    print('Adding 3 points')
                    mean_final = mean_final + 3

            if (20 <= Weather_clime <= 30):
                if ((crop == "Oilseeds") or (crop == 'Tea')):
                    mean_final = mean_final + 3

            if (10 <= Weather_clime <= 15):
                if ((crop == "Wheat")):
                    mean_final = mean_final + 3

            if (21 <= Weather_clime <= 27):
                if ((crop == "Sugercane")):
                    mean_final = mean_final + 3

            if (21 <= Weather_clime <= 35):
                if ((crop == "Groundnut")):
                    mean_final = mean_final + 3

            if (21 <= Weather_clime <= 35):
                if ((crop == "Groundnut")):
                    mean_final = mean_final + 3

            if (12 <= Weather_clime <= 25):
                if ((crop == "Barley")):
                    mean_final = mean_final + 3

            if (7 <= Weather_clime <= 20):
                if ((crop == "Sorghum")):
                    mean_final = mean_final + 3

            if (18 <= Weather_clime <= 27):
                if ((crop == "Maize")):
                    print("added thre")
                    mean_final = mean_final + 3


            mean_final=abs(mean_final)
            print("MEan", mean_final)

            import pandas as pd

            dataset = pd.read_csv("cultivo_main/total.csv")
            Output = dataset.groupby(['commodity'])
            # print(Output.groups)
            per = Output.get_group(crop)
            print(per.shape)
            a, b = per.shape
            print(per.min_price)
            print(sum(per.min_price) / a)
            min = sum(per.min_price) / a
            max = sum(per.max_price) / a
            mod = sum(per.modal_price) / a
            min=float("{0:.3f}".format(min))
            max = float("{0:.3f}".format(max))
            mod = float("{0:.3f}".format(mod))

            print("min", min)
            print("max", max)
            print("mod", mod)


           # print("Final Average Outcome", mean_final)
            final_outcome = float("{0}".format(mean_final))
            final_main = str(final_outcome).split('.')[0]
            final_dec = str(final_outcome).split('.')[1]

            obj = prod_area.objects.filter(district=area)
            d = finding_subs(obj, crop)
            dd = list(d[i] for i in d)
            dd = list(map(float, dd))
            dd.sort(reverse=True)
            fin_dict = {}
            for i in dd:
                for j in d:
                    if float(d[j]) == i:
                        fin_dict[j] = i

            for i in fin_dict:
                fin_dict[i] = round(fin_dict[i], 5) * 100
                fin_dict[i] = float("{0:.3f}".format(fin_dict[i]))

            print("fin dict",fin_dict)

            regression3 = str(round(regression3, 2))
            print("regression3", regression3)

            p1 = str(round(p1, 2))
            print("p1", p1)

            final_dec = final_dec[0:2]
            print("p1", final_dec)

            Regressed_Fertilizers=str(Regressed_Fertilizers)

            agriResult['ditrict'] = area
            agriResult['crop'] = crop
            agriResult['regre1'] = regre1
            agriResult['regre3'] = regression3
            agriResult['first'] = p1
            agriResult['third'] = p3
            agriResult['temp_det'] = temp_det
            agriResult['final'] = final_outcome
            if(int(final_main)>100):
              agriResult['finalout_main'] = 99
            else:
                agriResult['finalout_main'] = final_main

            agriResult['finalout_dec'] = final_dec
            agriResult['ff'] = fin_dict
            agriResult['Regressed_Fertilizers']=Regressed_Fertilizers
            agriResult['rate'] = rate
            agriResult['min'] = min
            agriResult['max'] = max
            agriResult['mod'] = mod

            import json
            from django.core.serializers.json import DjangoJSONEncoder

            traildata = json.dumps(agriResult, cls=DjangoJSONEncoder)
            request.session['forReport'] = traildata

            return render(request, 'cultivo_main/parallax.html', {'agrix': agriResult})
        else:
            return render(request, 'cultivo_main/new.html', {'crop': crop})



    else:
        raise Http404("You are unauthorised to access this page")

        # =====================================================for making the final prediction====================================


# ===================================================FOR IMPORTING CSV FILES TO DJANGO DBS============================================


def simple_upload(request):
    if request.method == 'POST':
        value = True

        res = predone()
        value = vv(res)

        if value == False:
            res = prodarea()
            value = vv(res)

        if value == False:
            res = one()
            value = vv(res)

        if value == False:
            res = two()
            value = vv(res)

        if value == False:
            res = three()
            value = vv(res)

        if value == False:
            res = pred_three()
            value = vv(res)

    return render(request, 'core/simple_upload.html')


def vv(request, res):
    dataset = Dataset()
    new = request.FILES['myfile']

    imported_data = dataset.load(new.read())
    result = res.import_data(dataset, dry_run=True)  # Test the data import

    if not result.has_errors():
        value = True
        res.import_data(dataset, dry_run=False)  # Actually import now

    else:
        value = False
    return value


def input(request):
    return render(request, 'cultivo_main/footer.html')


def login1(request):
    global loginFlag, loginUser
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        request.session['username'] = username
        print(username, password)
        message = ""

        if len(Users.objects.filter(emp_id=username)) == 0:
            message = message + "No Matching Accounts Found"
        else:
            pass_hash = str(Users.objects.filter(emp_id=username)[0]).split(";")[4]
            decrypt_text = pass_hash
            if password == decrypt_text:
                message = message + "Welcome to the Home Page"
                loginFlag = True
                loginUser = username
                print(loginUser)
                return render(request, 'cultivo_main/footer.html')
            else:
                message = message + "Wrong Password Entered"

        print(message)
        context = {"message": message}
        return render(request, 'cultivo_main/UserFailure.html', context)

    return render(request, 'cultivo_main/login.html')


def register(request):
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()

        emp_id = request.POST['emp_id']
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        ques_1_id = request.POST['ques_1_id']
        ans_1 = request.POST['ans_1']
        ques_2_id = request.POST['ques_2_id']
        ans_2 = request.POST['ans_2']
        gender = request.POST['gender']
        phone = request.POST['phone']
        repeat_password = request.POST['repeat_password']
        print(emp_id, name, password, email, ques_1_id, ans_1, ques_2_id, ans_2, gender, phone, repeat_password)
        count = 0
        message = ""
        searchObject = Users.objects.all()
        flag = 1
        for i in range(len(searchObject)):
            lst = str(searchObject[i]).split(";")
            print(lst[0], emp_id)
            if lst[0] == emp_id:
                message = message + "Employee already exists.\n"
                flag = 0
                break
        if flag == 1:
            count = count + 1

        if password == repeat_password:
            if len(password) > 6:
                flag1, flag2, flag3 = 0, 0, 0
                for i in range(len(password)):
                    ele = ord(password[i])
                    if ele > 96 and ele < 123:
                        flag1 = 1
                    elif ele > 47 and ele < 58:
                        flag2 = 1
                    elif ele > 64 and ele < 91:
                        flag3 = 1
                if flag1 == 1 and flag2 == 1 and flag3 == 1:
                    count = count + 1
                else:
                    message = message + "Re-enter the Password.\n"
        else:
            message = message + "Passwords does not match.\n"

        print(count)
        if count == 2:
            raw_text = password
            encrypt_text = raw_text
            Users(emp_id=emp_id,
                  name=name,
                  password=encrypt_text,
                  email=email,
                  ques_1_id=ques_1_id,
                  ans_1=ans_1,
                  ques_2_id=ques_2_id,
                  ans_2=ans_2,
                  gender=gender,
                  phone=phone).save()

            message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}
        return render(request, 'cultivo_main/register.html', context)

    else:
        message = "Welcome To Registration Page"
        context = {"message": message}
        return render(request, 'cultivo_main/register.html', context)


def Generate_Report(request):
    print("Its in Email Report part")

    import smtplib
    import email.message
    import smtplib
    import email.message

    user = request.session['username']
    print("user", user)

    from .models import Users

    returned = Users.objects.get(emp_id=user)

    print("Returned ", returned.email)

    usermail = returned.email

    print(request.session['forReport'])
    forReport = request.session['forReport']
    print("ForReport ", forReport)
    print(type(forReport))

    import json

    json_acceptable_string = forReport.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    print(d)

    server = smtplib.SMTP('smtp.gmail.com:587')
    import datetime
    email_content = """\
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

       <title>Location Based Crop suggested Report</title>
       <style type="text/css">

       </style>
    </head>

    <body>


    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="grey"><tr><td>
    <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p><a href="#">View in Browser</a></p>
          </td>
        </tr>
      </table>

    <table id="main" width="600" align="center" cellpadding="0" cellspacing="15"  bgcolor="ffffff">
        <tr>
          <td>
            <table id="header" cellpadding="10" cellspacing="0" align="center" background="" bgcolor="8fb3e9">
              <tr>
                <td width="570" align="center"  bgcolor="grey"><h1>Data Reporting - Success Rate: {12} % </h1></td>
              </tr>
              <tr>
                <td width="570" align="right" bgcolor="lightgreen"><p>{0}</p></td>
              </tr>
            </table>
          </td>
        </tr>

        <tr>
          <td>
            <table id="content-3" cellpadding="0" cellspacing="0" align="center">
              <tr>
                  <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                  <img src="https://lucidgreen.io/wp-content/uploads/gettyimages-1135398660-170667a__FocusFillWzExNzAsNjU4LCJ5Iiw2MF0.jpg" width="350" height="250"  />
                </td>
                  <td width="15"></td>
                <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                    <img src="https://technostacks.com/wp-content/uploads/2018/10/machine-learning-farming-robot.jpg" width ="350" height="250" />
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td>
            <table id="content-4" cellpadding="0" cellspacing="0" align="center">
              <tr>
                <td width="200" valign="top">
                  <h3>Insights about Location</h3>
                  <p>District : {1}</p>
                  <p>Temperature : {2}</p>

                  <p>Longitude : {3}</p>
                  <p>Latitude : {4}</p>
                  <p>Humidity : {5}</p>
                  <p>Air Pressure : {6}</p>
                  <p>Wind Speed : {7}</p>
                </td>
                <td width="15"></td>
                <td width="200" valign="top">
                  <h3>Insight about Crop</h3>

                   <p>Crop : {8}</p>
                   <p>Production  : {9}</p>
                   <p>Export  : {10}</p>
                   <p>Import  : {11}</p>
                    <p>Fertilizers Used for perticuler crop  : {12}</p>
                     <p>Increment in Success Rate is  : {13}%</p>
                      <p>Min Price is  : {14}/p>
                       <p>Max Price  is  : {15}</p>
                        <p>Mod Price is  : {16}</p>
                     <p>Average usage : 35KG/1 Hector</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>


      </table>
      <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p>{0} Design better experiences for web & mobile</p>
            <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
          </td>
        </tr>
      </table><!-- top message -->
    </td></tr></table><!-- wrapper -->

    </body>
    </html>


    """.format(datetime.date.today(), d['ditrict'], d['temp_det']['temperature'], d['temp_det']['longitude'],
               d['temp_det']['latitude'], d['temp_det']['humidity'], d['temp_det']['pressure'],
               d['temp_det']['windspeed'], d['crop'], d['production'], d['export'], d['import'], d['finalout_main'],
               d['Regressed_Fertilizers'],d['rate'],d['min'],d['max'],d['mod'])

    msg = email.message.Message()
    msg['Subject'] = 'A.I generated Report'

    msg['From'] = 'anilkumardv.ani@gmail.com'
    msg['To'] = usermail
    password = "anu.a0312"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    server = smtplib.SMTP('smtp.gmail.com:587')

    return render(request, 'cultivo_main/Generated.html')

