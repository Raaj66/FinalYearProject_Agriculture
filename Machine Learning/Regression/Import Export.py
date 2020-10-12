import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
datset = pd.read_csv("Dataset3.csv")
datset_crop = datset.drop_duplicates('crop')['crop']  ##Removed Duplicates
#print("Dataset_crop",datset_crop)  ##Keeps 1st in row

print(datset_crop)

# col_Names=["Sequence", "Start", "End", "Coverage"]
# my_CSV_File= pd.read_csv("Output3.csv",names=col_Names)

def fit(x, y, crop, d):
    ppp = []
    regressor = RandomForestRegressor()
    for i in range(10):
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=i * 13)
        regressor.fit(xtrain, ytrain)
        predy = regressor.predict(xtest)
        print("RMS",mean_squared_error(ytest,predy))
        ppp.append(predy.mean())
    d[crop] = ppp
    return d
production = {}
imports = {}
exports = {}


for i in datset_crop:
    dis_val = datset.loc[(datset['crop'] == i)]
    print("dis val",dis_val)

    x1 = dis_val.iloc[:, 7:8].values  # seed
    #print("x1",x1)  Production
    y1 = dis_val.iloc[:, 2:3].values  # production
    # print("y1",y1)   Seeds
    production = fit(x1, y1, i, production)
    print("prodcution",production)
    ###Upto here Production

    a = dis_val.iloc[:, 4:6]   #Stock,Export,
    b = dis_val.iloc[:, 2:3]   #Production
    # print("aa",a)
    # print("bb",b)
    x2=b+a
    #print('x2 before',x2)
    x2['Production'] = b.iloc[:, 0]
    x2['Export'] = a.iloc[:, 0]

    x2['Stock'] = a.iloc[:, 1]
   # print( x2)  ##Its arranging the colloumns alphabeticallys

    for k in list(a.iloc[0:0]):  ###looping throuh Export
        print('kk',k)          #
        x2[k] = a[k]
        print(x2)

    y2 = dis_val.iloc[:, 3:4].values  #imports
    print('y2', y2)
    imports = (fit(x2.values, y2, i, imports))
    print("Imports",imports)

    a = dis_val.iloc[:, 2:4]  ##prodcution and import
    b = dis_val.iloc[:, 7:8]  ##seed
    print('b', b)

    x3 = b + a
    x3['Production'] = a.iloc[:, 0]
    x3['Imports'] = a.iloc[:, 1]

    x3['Seed'] = b.iloc[:, 0]
    print('x3', x3)
    for k in list(a.iloc[0:0]):
        x3[k] = a[k]

    y3 = dis_val.iloc[:, 5:6].values  ###exportss
    print("y3",y3)
    exports = (fit(x3.values, y3, i, exports))
    print("exports",exports)


mean_prod = {}
mean_import={}
mean_export={}
output=[]


def mean(input):
 sum=0
 for i in input:
     sum = sum + i
     print(sum)
 return sum/10


for i in datset_crop:
        l = []
        mean_prod[i] = mean(production[i])
        mean_import[i]=mean(imports[i])
        mean_export[i]=mean(exports[i])
        l.append(i)

        l.append( mean_prod[i])
        l.append( mean_import[i])
        l.append(mean_export[i])

        output.append(l)
print("Its Working")
popo = pd.DataFrame(output)
popo.rename(columns={0: 'Crop',
                   1: 'Production',
                   2: 'imports',
                   3: 'exports',

                   }, inplace=True)

popo.to_csv('Output3.csv')


