import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 1234
s.bind(('',12344))
while(True):
	msg=input()
	s.sendto(msg.encode(),('localhost',port))
	if msg=='stop':
		break
	m1,addr=s.recvfrom(1024);
	print(m1.decode());
	
