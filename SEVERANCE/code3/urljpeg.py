import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
PICTURE = 'cover3.jpg'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

cmd = f'GET http://{HOST}/{PICTURE} HTTP/1.0\r\n\r\n'
mysock.sendall(cmd.encode())

count = 0
picture = b""
while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count  += len(data)
    print(len(data), count)
    picture += data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
