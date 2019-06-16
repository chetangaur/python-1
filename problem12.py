#! /usr/bin/python3
import webbrowser
from googlesearch import search
import pyqrcode
import os

data=input("enter you want to search ")
webbrowser.open_new_tab('https://www.google.com/search?q='+data)

list=[]
for i in search(data,stop=3):
	list.append(i)
print(list)

j=0
for i in list:
	a=pyqrcode.create(i)
	j=j+1
	a.svg(str(j)+"qr.svg",scale=8)
d=input(" name of html file ")
os.system('touch'+' ' +d)
os.system('echo "<html><h1>qr codes:</h1><body><img src="1qr.svg"><img src="2qr.svg"><img src="3qr.svg"></body></html>"  >'+d)

os.system('mv '+d+' /var/www/html/')
os.system('mv 1qr.svg /var/www/html/')
os.system('mv 2qr.svg /var/www/html/')
os.system('mv 3qr.svg /var/www/html/')




