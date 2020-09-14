
import sys #allows us to enter command line args
import socket
from datetime import datetime

#define our target

if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments.")
	sys.exit()
