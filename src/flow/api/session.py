from requests import Session as reqSession
from bs4 import BeautifulSoup as bs
import os
import re
import datetime
import pickle
from dotenv import load_dotenv
load_dotenv(dotenv_path="../../.env")

print(os.getenv("EMAIL"))

class Session:
    def __init__(self, base, debug):
        self.debug = debug
        self.sessionFile = "/home/stevee/px/united-domains/src/flow/api/session.cookie"
        self.maxSessionTimeSeconds = 30 * 60
        self.base = base
        self.loadSession()

    def isAuthenticated(self):
        res = self.s.get("%s/portfolio" % self.base)
        return True if "Kunden-Nr:" in str(res.content) else False

    def saveSession(self):
        with open(self.sessionFile, "wb") as f:
            pickle.dump(self.s, f)
            if self.debug: print("[+] Saved session") 


    def loadSession(self):
        self.s = reqSession() 
        if os.path.exists(self.sessionFile):
            time = datetime.datetime.fromtimestamp(os.path.getmtime(self.sessionFile))
            if (datetime.datetime.now() - time).seconds < self.maxSessionTimeSeconds:
                if self.debug: print("[+] Session found, that is not too old") 
                with open(self.sessionFile, "rb") as f:
                    if self.debug: print("[+] Session loaded") 
                    self.s = pickle.load(f)


    def authenticate(self):
        res = self.s.get("%s/login" % self.base)
        bs_content = bs(res.content, "html.parser")
        csrf = bs_content.find("form", {"id":"order-login-form"}).find("input", {"name": "csrf"})["value"]
        csrfmeta = bs_content.find("meta",{"name":"csrf"})["content"]
        csrfscript = re.search(r'(?<=\"CSRF_TOKEN\":\")[^\"]*(?=\")' ,str(bs_content.find("head"))).group()

        headers = {"HTTP-X-CSRF-TOKEN": csrfmeta, "Referer":"https://www.united-domains.de/login/"}
        print(headers)
        lang = self.s.post("%s/set-user-language" % self.base, {"language":"en-US"}, headers=headers)
        print("%s/set-user-language" % self.base)

        print( "[+] Set lang to de" if self.s.post("%s/set-user-language" % self.base, {"language":"en-US"}, headers=headers).status_code == 200 else "[-] Failed to set lang")
        self.s.post("%s/sync-session/request" % self.base, {"method":"GET","uri":"/login/","referrer":""}, headers=headers)


        login_data = {"csrf":csrf, "selector":"login","email":os.getenv("EMAIL"), "pwd":os.getenv("PASSWORD"), "submit":"Login"}    
        
        # save response to extract csrf for totp
        auth_site = self.s.post("%s/login" % self.base, login_data)
        auth_content = bs(auth_site.content, "html.parser")

        errorMsg = auth_content.find("div",{"class":"callout"}).findNext("li").text

        if ("versuchen" in errorMsg):
            raise Exception("Username or Password wrong")
            
        if ("Login-Versuche" in errorMsg):
            raise Exception("Too many wrong trys")

        else:
            if (os.getenv("ISTOTPON")):
                totp = input("[!] Enter totp: ")
                csrf = auth_content.find("input", {"name": "csrf"})["value"]
                login_data = {"totp": totp, "submit": "Login",
                          "csrf": csrf}
                #ToDo implement wrong totop
                print(self.s.post("%s/login" % self.base, login_data).status_code)
            else:
                print("[+] Login worked")

            self.saveSession()

