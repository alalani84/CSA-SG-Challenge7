# from webexteamssdk import WebexTeamsAPI
import requests
import json

meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

msversion = '11.31'
mrversion = '26.6.1'
mxversion = '15.27'
mvversion = '4.0'
WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli"
myWebexToken = ""  # you will need to put your personal token here

baseurl = "https://dashboard.meraki.com/api/v0/networks/"

payload = {}
headers = {
    'Accept': 'application/json',
    'X-Cisco-Meraki-API-Key': meraki_api_key,
}

url = baseurl + mynetwork + '/devices'  # finish the url!

response = requests.get(url=url, headers=headers)

myresponse = response.json()

mx = 0
ms = 0
mr = 0
mv = 0
i = 0
m = []
s = []

for devices in myresponse:
    model = devices['model']
    firmware = devices['firmware']
    serial = devices['serial']

    if model[:2] == "MS" and firmware[7:].replace('-', '.') == msversion:
        ms = ms + 1
    elif model[:2] == "MX" and firmware[6:].replace('-', '.') == mxversion:
        mx = mx + 1
    elif model[:2] == "MR" and firmware[9:].replace('-', '.') == mrversion:
        mr = mr + 1
    elif model[:2] == "MV" and firmware[7:].replace('-', '.') == mvversion:
        mv = mv + 1
    else:
        m.append(model)
        s.append(serial)


print("Total switches that meet standard: {}".format(ms))
print("Total APs that meet standard: {}".format(mr))
print("Total Security Appliances that meet standard: {}".format(mx))
print("Total Cameras that meet standard: {}".format(mv))
print("Devices that will need to be manually checked:")
for i in range(len(m)):
    print('Serial#: {}, Model#: {}'.format(s[i], m[i]))
