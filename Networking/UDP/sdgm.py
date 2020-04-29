import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 1234
s.bind(('',port))
data,addr = s.recvfrom(1024)
while(True):
	if(data.decode() == 'stop'):
		break
	print ('Message is ',data.decode())
	send=input()
	s.sendto(send.encode(),('localhost',12344))
	data,addr=s.recvfrom(1024)

