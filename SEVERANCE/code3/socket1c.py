import socket


def main():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url = input('please write URL: ')
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
    sdata = 0
    while True:
        data = mysock.recv(512)
        data = data.decode()
        ldata = len(data)
        if ldata < 1:
            break
        sdata += ldata
        if sdata > 3000:
            prevec = sdata - 3000
            sdata -= prevec
            print(data[:-prevec])
            break
        print(data, end='')
    print(f'in total {sdata} characters')
    mysock.close()


if __name__ == '__main__':
    main()