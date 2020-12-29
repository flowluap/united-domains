import datetime
import pickle
import os
from flow.api.session import Session
from flow.api.cachedRequest import cR, cRPost


class Api:
    def __init__(self, debug):
        self.base = "https://www.united-domains.de"
        self.debug = debug

        self.session = Session(self.base , self.debug)

    def makeAuthReq(self, url, data, method, cached=True):
        if (self.session.isAuthenticated()):
            if self.debug: print("[+] Session is authenticated")
            if (method == "GET"):
                if (cached):
                    return cR(self.session.s, url, self.debug)
                else:
                    return self.session.s.get(url)
            if (method == "POST"):
                if (cached):
                    return cRPost(self.session.s, url, data, self.debug)
                else:
                    return self.session.s.post(url, data)

        else:
            print("[-] Session is not authenticated, going to reauthenticate")
            self.session.authenticate()
            self.makeAuthReq(url, data, method, cached=cached)
