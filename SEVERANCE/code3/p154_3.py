import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

sdata = fhand.read()

sdata = sdata.decode()

jj = min(3000, len(sdata))

sdata = sdata[:3000]

print(sdata)
print(jj)
