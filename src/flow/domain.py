from bs4 import BeautifulSoup as bs
from flow.util.recordValidator import validateRecord
import re
import math


class Domain:
    def __init__(self, apiUtils):
        self.apiUtils = apiUtils

    def getSubDomains(self, domainId):
        res = self.apiUtils.makeAuthReq(
            "%s/pfapi/dns/domain/%d/subdomain-list" % (self.apiUtils.base, domainId), {}, "GET")
        return res.content

    def getRecords(self, domainId):
        res = self.apiUtils.makeAuthReq(
            "%s/pfapi/dns/domain/%d/records" % (self.apiUtils.base, domainId), {}, "GET")
        return res.content


    def removeRecord(self, domainId, record):
        res = self.apiUtils.makeAuthReq(
                "%s/pfapi/dns/domain/%d/records/remove" % (self.apiUtils.base, domainId), record, "PUT")


    def setRecord(self, domainId, record):
        validateRecord(record)
        res = self.apiUtils.makeAuthReq(
            "%s/pfapi/dns/domain/%d/records" % (self.apiUtils.base, domainId), record, "PUT")
        return res.content
