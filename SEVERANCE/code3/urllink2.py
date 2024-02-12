# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url = 'https://docs.python.org'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print()
    print()
    print('TAG:', tag)
    print('\nURL:', tag.get('href', None))
    print('\nCONTENTS', tag.contents)
    # try:
    #     print('\nCONTENTS', tag.contents[0])
    # except:
    #     print('\nCONTENTS: 000 000 000')
    print('\nATTRIBUTES:', tag.attrs)
