import time
logo = ('''
\033[39m  ---------------------------------------------------------
  
\033[32m  	
	 $$$$$$\     $$$$$\            $$\           
	$$  __$$\    \__$$ |           \__|          
	$$ /  $$ |      $$ |$$\    $$\ $$\  $$$$$$\  
	$$$$$$$$ |      $$ |\$$\  $$  |$$ |$$  __$$\ 
	$$  __$$ |$$\   $$ | \$$\$$  / $$ |$$ /  $$ |
	$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |$$ |  $$ |
	$$ |  $$ |\$$$$$$  |   \$  /   $$ |$$$$$$$  |
	\__|  \__| \______/     \_/    \__|$$  ____/ 
	                                   $$ |      
	                                   $$ |      
	                                   \__|      

\033[39m  ---------------------------------------------------------		
''')
for line in logo.splitlines():
    print(line)
    time.sleep(0.1)
print()
print()
import requests,re

number = str(input('\033[39m© \033[32mEnter Your Number \033[34m:\033[39m '))
password = str(input('\033[39m© \033[32mEnter Your Password \033[34m:\033[39m '))
print()
url = 'https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token'
headers = {
"Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "x-agent-operatingsystem": "10.1.0.264C185",
    "clientId": "AnaVodafoneAndroid",
    "x-agent-device": "HWDRA-MR",
    "x-agent-version": "2022.1.2.3",
    "x-agent-build": "500",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "142",
    "Host": "mobile.vodafone.com.eg",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.1"
}
data = 'username='+number+'&password='+password+'&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
setup = requests.post(url, headers=headers, data=data).json()
token = setup['access_token']

#print(token)

url = f"https://mobile.vodafone.com.eg/services/dxl/epo/eligibleProductOffering?customerAccountId={number}&type=MIProducts"
headers = {
    "api-host": "EligibleProductOfferingHost",
    "useCase": "MIProfile",
    "x-dynatrace": "MT_3_15_311683191_354-0_a556db1b-4506-43f3-854a-1d2527767923_811_23063_1366",
    "Authorization": f"Bearer {token}",
    "api-version": "v2",
    "x-agent-operatingsystem": "V11.0.8.0.QJWMIXM",
    "clientId": "AnaVodafoneAndroid",
    "x-agent-device": "curtana",
    "x-agent-build": "526",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "msisdn": number,
    "Accept-Language": "en",
    "Host": "mobile.vodafone.com.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.3"}
a = requests.get(url, headers=headers).text

#print(a)

dd = re.search('{"value":"Plus_58000MB","schemeName":"TechnicalID"},{"value":"(.*?)","schemeName":"EncProductID"}', a).group(1)

#print(dd)

url58="https://mobile.vodafone.com.eg/services/dxl/pom/productOrder" 
head58= {
    "api-host": "ProductOrderingManagement",
    "useCase": "MIProfile",
    "x-dynatrace": "MT_3_13_311683191_347-0_a556db1b-4506-43f3-854a-1d2527767923_0_22182_1205",
    "Authorization": f"Bearer {token}",
    "api-version": "v2",
    "x-agent-operatingsystem": "V11.0.8.0.QJWMIXM",
    "clientId": "AnaVodafoneAndroid",
    "x-agent-device": "curtana",
    "x-agent-version": "2022.11.1",
    "x-agent-build": "526",
    "Accept": "application/json",
    "msisdn": number,
    "Accept-Language": "en",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "612",
    "Host": "mobile.vodafone.com.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.3"}
data58= {"channel":{"name":"MobileApp"},"orderItem":[{"action":"add","product":{"characteristic":[{"name":"ExecutionType","value":"Sync"},{"name":"LangId","value":"en"},{"name":"MigrationType","value":"Repurchase"},{"name":"OneStepMigrationFlag","value":"Y"},{"name":"DropAddons","value":"True"}],"relatedParty":[{"id":number,"name":"MSISDN","role":"Subscriber"}],"id":"Plus_58000MB_GRACE","@type":"MI","encProductId":dd}}],"@type":"MIProfile"}
r58=requests.post(url58,headers=head58,json=data58).text
print('\033[39m✓ \033[32mDone add \033[39m58000 \033[32mMB Successfully \033[39m')
print(r58)
