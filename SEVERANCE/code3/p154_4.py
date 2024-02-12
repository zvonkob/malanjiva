
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://docs.python.org'

html = urllib.request.urlopen(url, context=ctx)
html = html.read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')

n = len(tags)

print(f'there are {n} paragraph tags <p>')


