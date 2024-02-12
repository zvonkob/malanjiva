# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url = 'http://www.dr-chuck.com/page1.htm'
print('i am reading', url)

html = urllib.request.urlopen(url, context=ctx).read()

pattern = b'href="(http[s]?://.*?)"'

links = re.findall(pattern, html)
for link in links:
    print(link.decode())
