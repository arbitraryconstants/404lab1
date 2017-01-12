#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/arbitraryconstants/404lab1/master/print_requests.py")

print response.text
print response.status_code

