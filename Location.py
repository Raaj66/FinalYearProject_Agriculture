import geocoder
g = geocoder.ip('me')
print(g.latlng)

import reverse_geocoder as rg
import pprint


import requests
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
print(my_ip)
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
print(geo_data)

import requests

res=requests.get("https://ipinfo.io/")
print(res.text)
