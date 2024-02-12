import socket


def main():
    #
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    host = 'data.pr4e.org'
    mysock.connect((host, 80))
    #
    cmd = f'GET http://{host} HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    #
    mysock.send(cmd)
    #
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    #
    mysock.close()


if __name__ == '__main__':
    main()