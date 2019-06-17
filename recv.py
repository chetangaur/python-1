#! /usr/bin/python36

import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024  - you can check free udp port using netstst -nulp command
#creating udp socket
#               ip type v4     , protcol type udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#fitting ip an dport with udp socket
s.bind((recv_ip,recv_port))
# s.bind() support tuple


while 4>2:
	# receive data from sender
	data=s.recvfrom(100)
	msg=data[0].decode('ascii')# covert byte-type into string
	print(msg)
	print(data[1])
	a=input("enter msg u want to send")
	b=a.encode('ascii')
        # sending data to sender
	s.sendto(b,data[1])

s.close()

