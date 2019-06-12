#! /usr/bin/python36

import subprocess
x=input("enter command: ")
y=subprocess.getstatusoutput(x)
f=open('hello.txt','+a')
f.seek(0)
data=f.read()
f.write(x)
f.write('/n')

f.close()

if 0 in y:
	print(y[1])
else:
	print("command not correct")

if x in data:
	subprocess.getoutput('echo not to do this again | festival --tts')
else:
	print("nothing")





