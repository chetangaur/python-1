#! /usr/bin/python36
import datetime
x=datetime.datetime.now()
y=x.hour

name=input("your name-")

if 0<=y<12:
	print("hello " +name+ " good mrng")
elif 12<=y<17:
	print("hello " +name+ " good afternoon")
elif 17<=y<20:
	print("hello " +name+ " good evening")
else:
	print("hello " +name+ " good night")


	

