

#! /usr/bin/python3
import string
import os
import crypt

string=input("username")


if string.isalpha():
	username=input('enter username')
	password='hello'+username
	encpass = crypt.crypt(password,'hi')	
	os.system("useradd -p " + encpass + " " + username)
	print("user created")

else:
	print("user cannot create")
