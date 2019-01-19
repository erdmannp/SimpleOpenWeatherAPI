#!/usr/bin/env python
# encoding: utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import requests
import json

API_KEY = ""
LOCATION = "Hannover,DE"


def main():
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s" % (LOCATION, API_KEY)
    myResponse = requests.get(url)
    if (myResponse.ok):
        j = json.loads(myResponse.content)
        print(j['main']['temp'])
    else:
        myResponse.raise_for_status()

if __name__ == "__main__":
    main()
