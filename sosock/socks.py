import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print(host)
port =4356           # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5) 
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection ', addr)
   s1="Hii "
   c.send(s1.encode())
   c.close()
