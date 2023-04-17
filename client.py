import socket
#from turtle import delay
import time


def Main():
	#host = '220.225.104.132'
	host = '192.168.10.132'
	port = 31051
	# host = '192.168.10.134'
	# port = 9988

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	
	
	
	message1 = '{"method":"select","datum":{"id":"99999"}}'
	message2 = '{"method":"insert","datum":{"id":"99999","name":"Aryan","address":"Mumbai","mobile":"45666"}}'
	message3 = '{"method":"update","datum":{"id":"99999","column":"address","value":"chennai"}}'
	message4 = '{"method":"delete","datum":{"id":"99999"}}'
	message5 = "GRANDLOTTO 123~1231 ***"
	message6 = "100 test_terminal~testconnectivity~testnumber***"
	l=[message6]
	for message in l:
		if message =='sleep':
			time.sleep(15)
		#message = input("enter anything : ")
		s.sendall(message.encode('utf8'))
		data = s.recv(8048)
		print('Received from the server :', str(data.decode('utf8')))
	s.close()

if __name__ == '__main__':
	Main()
