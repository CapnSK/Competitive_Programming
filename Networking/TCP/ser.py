import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = socket.gethostname()
port = 1234
s.bind(('',port))
s.listen(5)

c,addr = s.accept()
print('Connected to ',addr)
string = 'connection started'
by = string.encode()
c.send(by)
msg1 = c.recv(1024).decode()
while msg1!='stop':
	print(msg1)
	msg = input("Enter Message -> ")
	c.send(msg.encode())
	msg1 = c.recv(1024).decode()
c.close()
s.close()