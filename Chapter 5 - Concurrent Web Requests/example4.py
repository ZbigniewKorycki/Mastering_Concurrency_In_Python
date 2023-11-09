import threading
import requests
import time

class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None

    def run(self):
        respond = requests.get(self.url)
        self.result = f'{self.url}: {respond.text}'


urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]
start = time.time()

threads = [MyThread(url) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(thread.result)

print(f'Took {time.time() - start : .2f} seconds')
print('Done.')