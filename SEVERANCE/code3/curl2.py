import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

with open('cover3.jpg', 'wb') as g:

    size = 0
    while True:
        info = img.read(100000)
        if len(info) < 1:
            break
        size += len(info)
        g.write(info)

    print(size, 'characters copied.')
