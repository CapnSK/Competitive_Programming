import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1234
s.connect(('localhost',port))
strr = s.recv(1024)
print(strr.decode())
message = ''
while message != 'stop':
	message = input('Enter Message -> ')
	s.send(message.encode())
	message1 = s.recv(1024).decode()
	print(message1)
s.close()