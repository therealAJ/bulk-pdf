import re
import sys
import os
import requests
import argparse
from urllib.request import urlopen

'''
argparse to enable finicky command-line args
'''
parser = argparse.ArgumentParser()
parser.add_argument('website_url')
parser.add_argument('file_path')
parser.add_argument('relative_url', nargs='?', default='none')
args = parser.parse_args()

# HTML Parse URL 
url_link = str(args.website_url)
# wget URL
wget_link = str(args.relative_url)
# system path
sys_path = str(args.file_path)

website = urlopen(url_link)

# Decode website into string string
html = website.read().decode('utf-8')

#Find all local and non-hosted pdfs and download 
links = re.findall('"(https?://\S*?.pdf)"', html)
local_links = re.findall('"([^.\"=]*.pdf)', html)

#Download non-hosted PDFs
for link in links:
	command = 'wget'
	os.system("%s %s -P %s" % (command, link, sys_path))

#Download local/hosted PDFs
for link in local_links:
	command = 'wget'
	if(wget_link == 'none'):
		os.system("%s %s/%s -P %s" % (command, url_link, link, sys_path))
	else:
		os.system("%s %s/%s -P %s" % (command, wget_link, link, sys_path))
		