import socket


def main():
    #
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    # host, port = 'data.pr4e.org', 80
    host, port = 'localhost', 9000
    #
    mysock.connect((host, port))
    #
    cmd = f'GET http://{host}/page1.htm HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    #
    mysock.send(cmd)
    #
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        data = data.decode()
        print(data, end='')
    #
    mysock.close()


if __name__ == '__main__':
    main()