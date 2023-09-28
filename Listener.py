import socket
import sys
import time

def listen(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((ip, port))
	s.listen(1)
	print("Listening on port" + str(port))
	conn,addr = s.accept()
	print("Connection Received from", addr)
	while True:

		ans = conn.recv(1024).decode()
		sys.stdout.write(ans)
		command = input()


		command += "\n"
		conn.send(command.encode())
		time.sleep(1)


		sys.stdout.write("\033[A" + ans.split("\n")[-1])


listen("10.0.2.15",9999)
