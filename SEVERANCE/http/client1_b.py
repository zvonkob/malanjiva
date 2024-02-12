import socket

host, port = 'localhost', 9000
# host, port = '127.0.0.1', 9000

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))

cmd = f'GET http://{host}/romeo.txt HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    data = data.decode()
    print(data, end='')

mysock.close()
