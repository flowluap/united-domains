from bs4 import BeautifulSoup as bs
import re
import math

class Domains:
    def __init__(self, apiUtils):
        self.apiUtils = apiUtils

    def count(self):
        if self.apiUtils.debug: print("[+] Running countDomains")
        res = self.apiUtils.makeAuthReq("%s/portfolio/domainlist?seite=1&regdateFrom=&regdateTo=&pTyp=eigen&domainid=&displayConfDomain=1" % self.apiUtils.base, {}, "GET")
        content = bs(res.content, "html.parser")

        summed = re.search("\d+", content.find("div",{"id":"pfTableCounts"}).find("b").text).group()
        split = re.findall("\d+",content.find("div",{"id":"pfTableCounts"}).find("span").text)
        domiansPerPage = content.find("select",{"id":"settings_page_limit"}).find_all('option', selected=True)[0]["value"]

        return {"pages":math.ceil(int(summed)/int(domiansPerPage)) ,"sum":summed, "registered": split[0], "terminated":split[1], "transfer_failed":split[2]} 

    def getOld(self):
        if self.apiUtils.debug: print("[+] Running getDomains")
        domains = []
        
        for page in range(1, self.count()["pages"]+1):
            res = self.apiUtils.makeAuthReq("%s/portfolio/domainlist?seite=%d&regdateFrom=&regdateTo=&pTyp=eigen&domainid=&displayConfDomain=1" % (self.apiUtils.base, page), {}, "GET")
            content = bs(res.content, "html.parser")

            for domain in content.find("div",{"id":"pfTableContent"}).findAll("tr",{"class", "domainRow"}):
                name = domain.find("td", {"class":"td_domainName"}).find("a").text
                status = re.sub('\s+','', domain.find("td", {"class":"td-status"}).text)
                domainId = re.search("\d+", domain.find("td", {"class":"tdCheckbox"}).find("input")["name"]).group()
                domains.append({"name":name, "status":status, "domainId":domainId})
        return domains

    def get(self):
        res = self.apiUtils.makeAuthReq("%s/pfapi/domain-list" % self.apiUtils.base,{}, "GET")
        print(res.content)


