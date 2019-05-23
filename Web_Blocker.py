import time
from datetime import datetime as dt

websites=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"] 		#you can add any websies by adding inside the list. 
local_host="127.0.0.1" 		#write your local host( you can find it inside "hosts" file).
host_path=r"C:\Windows\System32\drivers\etc\hosts"		#path of your "hosts" file

start_time=8		#24 hours system(you can change it)
end_time=1		#24 hours system(you can change it)

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time): 		#it will check current time.
		print("working hours")
		with open(host_path,'r+') as f: 		#'r+' for read and write your host file.
			content=f.read() 		#read the host file.
			for web in websites: 
				if web in content: 		#if websites are inside the "hosts" file it will do nothing.
					pass
				else:
					f.write(local_host+" "+web+'\n') #if websites are not inside "host" file then it will write all those websites inside "hosts". 
	else:
		with open(host_path,'r+') as f:
			content=f.readlines() 		#reads every line of "hosts" file.
			f.seek(0) 		#it will move the cursor to the top-left(starting).
			for line in content:
				if not any(web in line for web in websites):
					f.write(line)
			f.truncate() 		#it will remove everything after the cursor.
		print("not working hours")
	time.sleep(5) 		#the loop is going to iterate every 5(five) second.
