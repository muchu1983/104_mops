"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
"""
Processor 模組負責整合資料工作
1. 取得 UI 輸入的訊息
2. 要求 Client 取得資料
3. 整合資料格式以符合本案要求
4. 產生 excel 檔
"""
from datetime import datetime
import re
import os
from mops.client import Client
from mops.client import MopsHtmlParser_1
from mops.client import MopsHtmlParser_2

class Processor:
    
    #建構子
    def __init__(self):
        self.fromDate = None
        self.toDate = None
        self.cli = Client()
    
    #設定並檢查日期
    def setDateRange(self, fromDate, toDate):
        try:
            self.fromDate = datetime.strptime(fromDate, "%Y%m%d")
            self.toDate = datetime.strptime(toDate, "%Y%m%d")
        except ValueError:
            print("日期格式錯誤，正確是：yyyymmdd")
            return False
        print("日期格式正確 from %s to %s" % (fromDate, toDate))
        return True
        
    #取得日期
    def getDateRange(self):
        if self.fromDate != None and self.toDate!= None:
            return (self.fromDate, self.toDate)
        else:
            return None
        
    #解析 p1_data.txt 取得 co_id DATE1 SKEY
    def parseP1DataLine(self, aLine):
        bLine = aLine.split("|#|#|#|")[4]
        kvDict = {}
        for cLine in bLine.split(";"):
            m = re.match(r"(.*)=(.*)" ,cLine) 
            if m != None:
                kvDict[m.group(1)] = m.group(2).strip("\"")
        ret = (kvDict["document.fm_t67sb07.co_id.value"],\
               kvDict["document.fm_t67sb07.DATE1.value"],\
               kvDict["document.fm_t67sb07.SKEY.value"])
        return ret
        
    #解析 temp_data.txt 取得 NameOfFund Buy/Sell NoOfUnits  Currency UnitPrice TotalAmount
    def parseTempData(self):
        if os.path.exists("temp_data.txt"):
            tempfile = open("temp_data.txt", "r", encoding="utf-8")
            nof = tempfile.readline().strip("\n")
            others = tempfile.readline().strip("\n") #暫不解析  TODO 
            tempfile.close()
            return (nof, others)
        else:
            return None
        
    #執行抓取網頁與分析程序
    def runProcess(self):
        dateRange = self.getDateRange()
        # template(SDATE, EDATE, YEAR1, YEAR2, MONTH1, MONTH2, SDAY, EDAY)
        form_template = "encodeURIComponent=1&step=2&TYPEK=pub&co_id_1=&SDATE=%s&EDATE=%s&YEAR1=%d&YEAR2=%d&MONTH1=%d&MONTH2=%d&SDAY=%d&EDAY=%d&scope=2&sort=1&rpt=bool_t67sb07&firstin=1"
        form_body = form_template % (dateRange[0].strftime("%Y%m%d"), #SDATE
                                     dateRange[1].strftime("%Y%m%d"), #EDATE
                                     dateRange[0].year - 1911, #YEAR1
                                     dateRange[1].year - 1911, #YEAR2
                                     dateRange[0].month, #MONTH1
                                     dateRange[1].year - 1911, #MONTH2
                                     dateRange[0].day, #SDAY
                                     dateRange[1].day) #EDAY
        res_t146sb10 = self.cli.requestServer("t146sb10", form_body)
        parser1 = MopsHtmlParser_1(convert_charrefs=True)
        parser1.feed(res_t146sb10) #p1_data.txt file 已建立
        p1file = open("p1_data.txt", "r", encoding="utf-8")
        c = 0
        for aLine in p1file:
            c = c+1
            print(c)
        p1file.close()
        
            #self.psr.parseP1DataLine(aLine)
        
        
        