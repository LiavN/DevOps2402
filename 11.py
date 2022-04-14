import datetime
import requests

def urlStatus(requested_url):
    try:
        return requests.get(requested_url).status_code
    except requests.exceptions.InvalidSchema as e:
        return str(e.args)

print(urlStatus("http://google.co.il"))

