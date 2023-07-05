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
import requests
try :
	import html2text
except :
	import os
	os.system('pip install html2text')
import re
import random
codrf = int(input('\033[39m© \033[32mEnter Your Code \033[34m:\033[39m '))
print()
time.sleep(9999999)
exit() 
for anas in range(100):
	def generate():
	    email_address = requests.get(
	        "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", timeout=6).json()[0]
	    return email_address
	
	def refresh(username, domain):
	    email_address = f"{username}@{domain}"
	    response = requests.get(
	        f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}", timeout=6).json()
	    if response:
	        files = []
	        email_id = response[0]["id"]    
	        response_msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={email_id}", timeout=6).json()
	        ccd = response_msg['textBody']
	        match = re.search(r"OTP: #(\d+) #", ccd)
	        otp = match.group(1)
	        a = 'abcdefghijklmnopqrstuvwxyz'
	        b = '0123456789'
	        vc = random.choice(a)+random.choice(a)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(a)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(a)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)
	        phone_brands = ['Samsung', 'Huawei', 'Xiaomi', 'Oppo', 'Realme', 'Apple', 'Sony', 'LG', 'Nokia', 'Motorola', 'Lenovo', 'OnePlus', 'Google', 'Asus', 'HTC', 'BlackBerry', 'Panasonic', 'ZTE', 'Vivo', 'Micromax']
	        typfh = random.choice(phone_brands)
	   #     print(otp)
	        headers8 = {'Content-Type': 'application/json','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-T585 Build/M1AJQ)','Host': 'hall.kinglion.link','Connection': 'Keep-Alive'}
	        data2 = {"account":email_address,"password":"12345678","sms_code":otp,"parent_user_id":codrf,"channel_id":5000,"ep_code":vc,"ep_name":typfh,"ep_type":2,"login_type":2}
	        response1 = requests.post('https://hall.kinglion.link/register', headers=headers8, json=data2)
	        if '"code":0' in response1.text:
	        	print('\033[39m✓ \033[32mDone add \033[39m3000 \033[32mCoins  Successfully ')
	        elif '今日IP注册人数达到上限' in response1.text :
	        	input('\033[33mchange  \033[39mip \033[33mand press enter >> ')
	        else :
	        	print('\033[31mError')
	        	exit()
	        #print(response1.text)
	
	        email_from = response_msg["from"]
	        email_subject = response_msg["subject"]
	        email_date = response_msg["date"]
	        email_html = response_msg["htmlBody"]
	        email_text = html2text.html2text(email_html)
	        attachments = response_msg["attachments"]
	        if attachments:
	            files = [attachment["filename"] for attachment in attachments]
	        return [email_id, email_from, email_subject, email_date, email_text, files]
	    return "No Messages Were Received.."
	
	def main():
	    email_address = generate()
#	    print(email_address)
	    headers0 = {'Content-Type': 'application/json','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-T585 Build/M1AJQ)','Host': 'hall.kinglion.link','Connection': 'Keep-Alive'}
	    data0 = {"account":email_address,"phone_area":"+52","channel_id":5000}
	    response0 = requests.post('https://hall.kinglion.link/inner/code/sendCodeForReg', headers=headers0, json=data0)
#	    print(response0.text)
	    while True:
	        message = refresh(email_address.split('@')[0], email_address.split('@')[1])
	        if message != "No Messages Were Received..":
	        #    print(message)
	            break
	
	if __name__ == "__main__":
	    main()
