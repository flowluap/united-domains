import os
import re
import time
from random import randint

production = True
cacheFolder = "./cache"

class Request:
    def __init__(self, content, status_code):
        self.status_code = status_code
        self.content = content


def cR(s, url, debug):
    clean_url = re.sub('[^A-Za-z0-9]+', '', url)
    if os.path.exists(cacheFolder):
        f = '%s/%s' % (cacheFolder, clean_url)

        if os.path.isfile(f):
            with open(f) as fopen:
                if debug: print("[+] Opening file from cache: "+url)
                return Request(fopen.read(), -1)
        else:
            with open(f, "w") as fopen:
                if production:
                    time.sleep(randint(1, 5))

                res = s.get(url)
                fopen.write(res.text)
                if debug: print("[+] Adding file to cache: "+url)
                return res
    else:
        os.mkdir(cacheFolder)


def cRPost(s, url, data, debug, cache=True):

    clean_url = re.sub('[^A-Za-z0-9]+', '', url+str(data))
    if os.path.exists(cacheFolder):
        f = '%s/%s' % (cacheFolder, clean_url)
        if not cache:
            if production:
                    time.sleep(randint(1, 5))
            return s.post(url, data).text
        elif os.path.isfile(f):
            with open(f) as fopen:
                if debug: print("[+] Opening file from cache: "+url)
                return Request(fopen.read(), -1)
        else:
            with open(f, "w") as fopen:
                if production:
                    time.sleep(randint(1, 5))
                res = s.post(url, data)
                fopen.write(res.text)
                if debug: print("[+] Opening file from cache: "+url)
                return res
    else:
        os.mkdir(cacheFolder)
