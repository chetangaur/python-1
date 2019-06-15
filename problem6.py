#! /usr/bin/python36

import os
option='''
press 1 to open file:
press 2 to open multiple files:
press 3 for cat -E:
press 4 for cat -n:
'''

print(option)
choice=input()
	
if choice  ==  '1' :
	d=input("file name ")
	f=open(d,'r')
	print(f.read())

elif choice  ==  '2' :
	x=[]
	s=int(input("enter no of files"))
	for i in range(s):
		d=input("file name ")
		x.append(d)
	print(x)

	for i in x:
		f=open(i,'r')
		print(f.read())
		f.close()
elif choice == '3' :
	d=input("enter file name ")
	f=open(d,'r')
	z=f.read()
	x=z.split('\n')
	print(x)
	
	for i in x:
		print(i+"$")

elif choice == '4' :
	d=input("enter file name ")
	f=open(d,'r')
	z=f.read()
	x=z.split('/n')
	print(x)
	j=1
	for i in x:
		print(j +i)
		j=j+1		

else:
	print("wrong")
