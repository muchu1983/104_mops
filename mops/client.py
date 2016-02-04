"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
from http.client import HTTPConnection
from html.parser import HTMLParser
import urllib.parse
import codecs

"""

"""
class Client:
    #構構子
    def __init__(self):
        self.conn = HTTPConnection("61.57.47.131", 80)

    #對 mops service 送出 POST
    def requestServer(self, ajaxService, form_body):
        headers = {"Accept":"*/*",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                   "Connection":"keep-alive",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Host":"mops.twse.com.tw",
                   "Origin":"http://mops.twse.com.tw",
                   "Referer":"http://mops.twse.com.tw/mops/web/" + ajaxService,
                   "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"}
        body = form_body
        self.conn.request("POST", "/mops/web/" + ajaxService, body, headers)
        res = self.conn.getresponse()
        res_raw = res.read()
        res_data = res_raw.decode("utf-8")
        return res_data

    #關閉連線
    def closeConnection(self):
        self.conn.close()
        
#解析 html
class MopsHtmlParser(HTMLParser):
    def __init__(self, **args):
        super(MopsHtmlParser, self).__init__(**args)
        self.inTr = False
        self.inTd = False
        self.trDataList = []
        self.tmpfile = codecs.open("data.txt", "a+", "utf-8")
        
    def feed(self, data):
        data = data.replace("<br>", "") #去除 <br> tag 以免影響 parse 
        super(MopsHtmlParser, self).feed(data)
        
    def __del__(self):
        self.tmpfile.close()
        
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.inTr = True
            self.trDataList = [] #準備新的list
        if tag == "td":
            self.inTd = True
        if tag == "input":
            if self.inTd and self.inTr == True:
                #print(attrs)
                pass
            
    def handle_endtag(self, tag):
        if tag == "tr":
            self.inTr = False
            if len(self.trDataList) == 4:
                self.tmpfile.write(str(self.trDataList)+"\n")
        if tag == "td":
            self.inTd = False
            
    def handle_data(self, data):
        if self.inTr and self.inTd == True:
            self.trDataList.append(data)
        