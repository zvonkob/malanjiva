from urllib.request import *


# host, port = 'localhost', 9000
host, port = 'data.pr4e.org', 80

pth = f'http://{host}:{port}/romeo.txt'
fhand = urlopen(pth)

for line in fhand:
    line = line.decode()
    line = line.strip()
    print(line)
