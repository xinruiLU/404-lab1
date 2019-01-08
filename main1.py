#!/usr/bin/env python


import requests


print(requests.__version__)

r = requests.get("http://www.google.com")
#print(r.status_code)
#print(r.headers)

github_url = "https://raw.githubusercontent.com/xinruiLU/404-lab1/master/main1.py"

r = requests.get(github_url)
print(r.text)




