#! /usr/bin/python36
import datetime
x=datetime.datetime.now().year
name=input("what is your name-")
age=int(input("age-"))

year=str((x-age)+95)
print(name + " will be 95 year old in " +year) 
# this is the best solution.
