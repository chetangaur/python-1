#! /usr/bin/python36
import os 

options='''
press 1 to create single file:
press 2 to create multiple files:
press 3 create no file:
'''
print(options)
choice=input()

if choice == '1' :
	d=input("file name")
	f=open(d,'+w')
	f.close()

elif choice == '2' :
	x=[]
	s=int(input("no of files u want to create "))
	for i in range(s):
		d=input("file name ")
		x.append(d)
	print(x)
	for i in x:
		f=open(i,'+w')

elif choice == '3' :
	d=input("enter file name ")
	print("comand excuted successfully")
		

else:
	print("wrong choice")
