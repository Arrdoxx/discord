import browser_cookie3
import requests
cookie_jar = browser_cookie3.chrome()
r = requests.get('https://vinted.fr', cookies=cookie_jar)
print(r.text)