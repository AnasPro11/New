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

url = f'https://web.vodafone.com.eg/services/dxl/epo/eligibleProductOffering?type=MIProducts&customerAccountId={number}'
headers = {
'Host': 'web.vodafone.com.eg',
 'Connection': 'keep-alive', 
 'Accept': 'application/json',
  'Authorization': f'Bearer {token}',
 'msisdn': number, 
 'Accept-Language': 'EN',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Content-Type': 'application/json',
  'Accept-Encoding': 'gzip, deflate, br'}
a = requests.get(url, headers=headers).text

#print(a)

dd = re.search('{"value":"Plus_58000MB","schemeName":"TechnicalID"},{"value":"(.*?)","schemeName":"EncProductID"}', a).group(1)

#print(dd)

url58='https://web.vodafone.com.eg/services/dxl/pom/productOrder'
head58={
"Host": "web.vodafone.com.eg",
"Connection": "keep-alive",
"Content-Length": "595",
"msisdn":number,
"Accept-Language": "AR",
"Authorization": f"Bearer {token}",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
"x-dtpc": "17$285342561_575h19vUAAECSRNINCSISMKQVKKPMBOROEKBBFP-0e0",
"Content-Type": "application/json",
"Accept": "application/json",
"clientId": "WebsiteConsumer",
"Origin": "https://web.vodafone.com.eg",
"Referer": "https://web.vodafone.com.eg/spa/flexManagement/internet"}
data58='{"channel":{"name":"MobileApp"},"orderItem":[{"action":"add","product":{"characteristic":[{"name":"ExecutionType","value":"Sync"},{"name":"LangId","value":"en"},{"name":"MigrationType","value":"Repurchase"},{"name":"OneStepMigrationFlag","value":"Y"},{"name":"DropAddons","value":"True"}],"relatedParty":[{"id":"%s","name":"MSISDN","role":"Subscriber"}],"id":"Plus_58000MB_GRACE","@type":"MI","encProductId":"%s"}}],"@type":"MIProfile"}' %(number,dd)
r58=requests.post(url58,headers=head58,data=data58).text
print('\033[39m✓ \033[32mDone add \033[39m58000 \033[32mMB Successfully \033[39m')
#print(r58)
