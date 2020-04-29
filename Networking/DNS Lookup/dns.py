import socket
try:
	ip = socket.gethostbyname(input('Enter Hosname : '))
	print(ip)

	name = socket.gethostbyaddr(ip)
	print(name)
except:
	print("Host not found")