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
        
#解析 t146sb10 response 將結果存入 p1_data.txt
class MopsHtmlParser_1(HTMLParser):
    def __init__(self, **args):
        super(MopsHtmlParser_1, self).__init__(**args)
        self.inTr = False
        self.inTd = False
        self.trDataList = []
        self.p1file = codecs.open("p1_data.txt", "w+", "utf-8")
        
    def feed(self, data):
        data = data.replace("<br>", "") #去除 <br> tag 以免影響 parse 
        data = data.replace("\n", "") #去除 \n 以免影響 parse 
        data = data.replace("\r", "") #去除 \r 以免影響 parse 
        data = data.replace("\t", "") #去除 \t 以免影響 parse 
        super(MopsHtmlParser_1, self).feed(data)
        
    def __del__(self):
        self.p1file.close()
        
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.inTr = True
            self.trDataList = [] #準備新的list
        if tag == "td":
            self.inTd = True
        if tag == "input": #解析 input
            if self.inTd and self.inTr == True and \
            len(attrs) == 3 and attrs[1] == ("value", "詳細資料"): 
                #value 為 "詳細資料"
                self.trDataList.append(attrs[2][1])
            
    def handle_endtag(self, tag):
        if tag == "tr":
            self.inTr = False
            if len(self.trDataList) == 5:
                for data in self.trDataList:
                    self.p1file.write(data+"|#|#|#|")
                self.p1file.write("\n")
        if tag == "td":
            self.inTd = False
            
    def handle_data(self, data):
        if self.inTr and self.inTd == True:
            self.trDataList.append(data)
        
#解析 t67sb03 將結果存入 temp_data.txt
class MopsHtmlParser_2(HTMLParser):
    def __init__(self, **args):
        super(MopsHtmlParser_2, self).__init__(**args)
        self.inTr = False
        self.inTd = False
        self.inTh = False
        self.isMoneyTdNext = False
        self.isFundTdNext = False
        self.tempfile = codecs.open("temp_data.txt", "w+", "utf-8")
        
    def __del__(self):
        self.tempfile.close()

    def feed(self, data):
        data = data.replace("<br>", "") #去除 <br> tag 以免影響 parse 
        data = data.replace("\n", "") #去除 \n 以免影響 parse 
        data = data.replace("\r", "") #去除 \r 以免影響 parse 
        data = data.replace("\t", "") #去除 \t 以免影響 parse 
        super(MopsHtmlParser_2, self).feed(data)
        
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.inTr = True
        if tag == "th":
            self.inTh = True
        if tag == "td":
            self.inTd = True
            
    def handle_endtag(self, tag):
        if tag == "tr":
            self.inTr = False
        if tag == "th":
            self.inTh = False
        if tag == "td":
            self.inTd = False
            
    def handle_data(self, data):
        if self.inTr and self.inTh and data == "交易單位數量、每單位價格及交易總金額":
            self.isMoneyTdNext = True
        if self.inTr and self.inTh and data == "標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）":
            self.isFundTdNext = True
        if self.inTr and self.inTd and (self.isMoneyTdNext or self.isFundTdNext):
            self.tempfile.write(data+"\n")
            self.isMoneyTdNext = False
            self.isFundTdNext = False