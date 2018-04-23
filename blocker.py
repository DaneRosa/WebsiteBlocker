#program for blocking websites during certain hours of the day on linux or macOS 
# this is a manual run via command line 
import time #This module provides various time-related functions
from datetime import datetime as dt #module supplies classes for manipulating dates and times in both simple and complex ways saved under dt

hosts_path = "/private/etc/hosts" #this is the path for linux and macOS users, replace if you have a custom setup
redirect ="127.0.0.1" 
website_list=["www.facebook.com", "facebook.com", "www.barstoolsports.com", "barstoolsports.com"] #this is an array of websites that I block from my machine during work hours. Add URLs that you wish

while True: #run the code
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt(dt.now().year, dt.now().month, dt.now().day, 16): #if datetime is between current day 8am and current day 4pm 
        #change the hours to be what you wish
        print("working hours") #if it is working hours print and:
        with open(hosts_path, 'r+') as file: #open the hosts file in "read and append" mode 
            content = file.read() #extract a string that contains all characters in the file
            for website in website_list: #look for websites within the website_list array 
                if website in content: #if the website already exists, pass 
                    pass
                else: #if it does not exist yet
                    file.write(redirect+ " " + website+"\n") #write the redirect and the website, break the line for multiple
    else: #if it is not within the current timeframe
        with open(hosts_path, "r+") as file: ##open the hosts file in "read and append" mode 
            content = file.readlines() #method readlines() reads until end of file (EOF)
            file.seek(0) #seek finds the very first position in the file instead of the last
            for line in content: #crawling our newly created content file
                if not any(website in line for website in website_list): #if you can't find any of the websites in the file
                        file.write(line) 
            file.truncate() #rewrite all of the lines starting at 0 
        print("fun hours") #tell the user its fun time
    time.sleep(5) #repeat every 5 seconds

