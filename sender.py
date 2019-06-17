#! /usr/bin/python36
import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024 -  you can check free udp using netstat -nulp command

#creating udp socket 
#               ip v4         , udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while 4>2: #while loop
	msg=input("enter msg u want to send..")
	nmsg=msg.encode('ascii') #change string into byte-like form
# sending data to receiver
	s.sendto(nmsg,(recv_ip,recv_port))
# receive data form rece. 
	print(s.recvfrom(100))
	
