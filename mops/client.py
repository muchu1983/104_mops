"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
from http.client import HTTPConnection
import urllib.parse
"""

"""
class Client:

    #構構子
    def __init__(self):
        self.conn = HTTPConnection("61.57.47.131", 80)

    #對 t146sb10 送出訊息
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

    #關閉 server 連線
    def closeConnection(self):
        self.conn.close()
        