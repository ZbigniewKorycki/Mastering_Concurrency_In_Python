import requests

url = 'http://www.google.com'
respond = requests.get(url)

print(respond.status_code)
print(respond.headers)

with open('google.html', 'w') as f:
    f.write(respond.text)

print('Done')