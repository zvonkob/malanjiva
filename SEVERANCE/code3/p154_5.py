import socket


def main():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # url = input('please write URL: ')
    url = 'http://data.pr4e.org/romeo.txt'
    try:
        host = url.split('/')[2]
    except:
        print('improperly formatted URL')
        return
    try:
        mysock.connect((host, 80))
    except:
        print('non-existnt URL')
        return
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
    sdata = ''
    while True:
        data = mysock.recv(512)
        data = data.decode()
        if len(data) < 1:
            break
        sdata += data
    mysock.close()
    sdata = sdata.strip()

    ii = sdata.find('\r\n\r\n')

    print(sdata[ii+4:])

if __name__ == '__main__':
    main()