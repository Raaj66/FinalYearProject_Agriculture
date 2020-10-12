import requests
import  datetime

print(datetime.date.today())



data=requests.get("https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=500")


print(data.json())

market_value=data.json()

if market_value['status']=='ok':
    print("Yes Server is on")
    records=market_value['records']
    #print(records)

    for i in records:
        print(i)