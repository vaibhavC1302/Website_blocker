import time 
from datetime import datetime as dt

host_path = r"C:\Windows\System32\Drivers\etc\hosts"
redirect = "127.0.0.1"
# add the websites you want to block in the website_list
website_list = ["www.facebook.com","facebook.com"]

while True :
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,16) :
        #these are the working hours(8:00 to 16:00)
        with open(host_path,"r+") as file :
            content = file.read()
            for website in website_list :
                if website in content :
                    pass
                else :
                    file.write(redirect + " " + website+"\n")
    else :
        with open(host_path,'r+') as file :
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list) :
                    file.write(line)
            file.truncate()
        print("fun hours...")
    time.sleep(5)