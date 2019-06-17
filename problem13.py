import sys
import datetime
import pyttsx3
import os
#1.
sound=pyttsx3.init()
sound.say("hello aditi")
sound.runAndWait()
#2.
x=datetime.datetime.now()
y=x.hour

def time(y):
	if 0<=y<12:
		print("hello aditi good morning")
	elif 12<=y<17:
		print("hello aditi good afternoon")
	elif 17<=y<20:
		print("hello aditi good evening")
	else:
		print("aditi good night")
time(y)

#3.
def add(*i):
	sum=0
	for k in i:
		sum=sum+k
	print(j)

#4.
def sort_numbers(*n):
	q=[]
	for l in n:
		q.append(l)
		q.sort()
	print(q)

#5.

def module_information():
	help('modules')
	print('total no. of moudules:')
	print(os.system('pip3 list | wc -l)

