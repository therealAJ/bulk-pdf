import re
import sys
import os
import requests
import argparse
from urllib.request import urlopen

parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument('b', nargs='?')
args = parser.parse_args()
print(args)

# Parse URL 
url_link = str(sys.argv[1])
# wget URL
wget_link = str(sys.argv[2])

website = urlopen(url_link)

# Decode website into string string
html = website.read().decode('utf-8')

#Find all local and non-hosted pdfs and download 
links = re.findall('"(https?://\S*?.pdf)"', html)
local_links = re.findall('"([^.\"=]*.pdf)', html)

for link in links:
	command = 'wget'
	path = str(sys.argv[2])
	os.system("%s %s -P %s" % (command, link, path))

for link in local_links:
	command = 'wget'
	path = str(sys.argv[3])
	os.system("%s %s%s -P %s" % (command, url_link, link, path))