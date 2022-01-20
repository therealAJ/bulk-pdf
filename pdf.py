import re
import os
import argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

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

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

website = urlopen(url_link, context=ctx)

# Decode website into string string
soup = BeautifulSoup(website.read(), features="html.parser")
links = []
local_links = []
divs = soup.find_all('a', attrs={'href': re.compile(".pdf$")})
for div in divs:
    href = div.get('href')
    if href.find("http") == -1:
        local_links.append(href)
    else:
        links.append(href)

# Download non-hosted PDFs
for link in links:
    command = 'wget'
    os.system("%s %s -P %s" % (command, link, sys_path))

# Download local/hosted PDFs
for link in local_links:
    command = 'wget'
    if(wget_link == 'none'):
        os.system("%s '%s/%s' -P %s" % (command, url_link, link, sys_path))
    else:
        os.system("%s '%s/%s' -P %s" % (command, wget_link, link, sys_path))
