from urllib.request import urlopen
import requests
import re
import sys
import os

website = urlopen(str(sys.argv[1]))

html = website.read().decode('utf-8')

links = re.findall('"(https?://\S*?.pdf)"', html)

for link in links:
    os.system('wget ' + link)