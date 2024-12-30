import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 4356             # Reserve a port for your service.

s.connect((host, port))
a=s.recv(1024)
print(a.decode()+" Your are Good looking")
s.close()