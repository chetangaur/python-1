#! /usr/bin/python36
from googlesearch import search

web=input("enter search")
y=[]

for i in search(web,stop=10):
         print(i)
         y.append(i)
print(y)
