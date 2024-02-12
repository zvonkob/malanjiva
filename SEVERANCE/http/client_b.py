from socket import *


def main():
    #
    client = socket(AF_INET, SOCK_STREAM)
    #
    # host, port = 'data.pr4e.org', 80
    host, port = 'localhost', 9000
    #
    try:
        client.connect((host, port))
    except Exception as exc:
        print('Error:', exc)
    #
    cmd = f'GET http://{host}/page1.htm HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    #
    client.send(cmd)
    #
    while True:
        data = client.recv(512)
        if len(data) < 1:
            break
        data = data.decode()
        print(data, end='')
    #
    client.close()


if __name__ == '__main__':
    main()