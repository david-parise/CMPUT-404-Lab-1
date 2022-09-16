import requests

req = requests.get("https://raw.githubusercontent.com/david-parise/CMPUT-404-Lab-1/main/curl.py")
print(req.text)
