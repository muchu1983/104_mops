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
import time
from random import randint
from mops.client import Client
from mops.client import MopsHtmlParser_1
from mops.client import MopsHtmlParser_2
from mops.xlwtwrapper import XlwtWrapper

class Processor:
    
    #建構子
    def __init__(self):
        self.fromDate = None
        self.toDate = None
        self.cli = Client()
        self.progress = 0
        self.progressObserver = []
    
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
        xlsfile = XlwtWrapper()
        dateRange = self.getDateRange()
        #form A template(SDATE, EDATE, YEAR1, YEAR2, MONTH1, MONTH2, SDAY, EDAY)
        formA_template = "encodeURIComponent=1&step=2&TYPEK=pub&co_id_1=&SDATE=%s&EDATE=%s&YEAR1=%d&YEAR2=%d&MONTH1=%d&MONTH2=%d&SDAY=%d&EDAY=%d&scope=2&sort=1&rpt=bool_t67sb07&firstin=1"
        formA_body = formA_template % (dateRange[0].strftime("%Y%m%d"), #SDATE
                                       dateRange[1].strftime("%Y%m%d"), #EDATE
                                       dateRange[0].year - 1911, #YEAR1
                                       dateRange[1].year - 1911, #YEAR2
                                       dateRange[0].month, #MONTH1
                                       dateRange[1].year - 1911, #MONTH2
                                       dateRange[0].day, #SDAY
                                       dateRange[1].day) #EDAY
        res_t146sb10 = self.cli.requestServer("t146sb10", formA_body)
        self.cli.closeConnection()
        parser1 = MopsHtmlParser_1(convert_charrefs=True)
        parser1.feed(res_t146sb10) #p1_data.txt file 已建立
        p1file = open("p1_data.txt", "r", encoding="utf-8")
        lines = len(p1file.readlines())#總筆數計算執行進度 (pointer 已被移到EOF)
        p1file.seek(0) #pointer 移到最開始位置
        handledLine = 0
        for aLine in p1file:#逐行解析
            handledLine = handledLine+1
            self.progress = int((handledLine/lines)*100)
            for ob in self.progressObserver:#通知 observer 目前進度
                ob.updateProgress(self.progress) #observer 需實作 updateProgress
            if handledLine%100 == 0:
                time.sleep(randint(30, 60))#每100筆資料休息30-60秒
            time.sleep(randint(1, 3))#每筆資料休息1-3秒
            (co_id, DATE1, SKEY) = self.parseP1DataLine(aLine)
            #form B template (co_id, DATE1, SKEY)
            formB_template = "encodeURIComponent=1&step=2&TYPEK=pub&co_id=%s&DATE1=%s&SKEY=%s&firstin=1"
            formB_body = formB_template % (co_id, DATE1, SKEY)
            try:
                res_t67sb03 = self.cli.requestServer("t67sb03", formB_body)
            except Exception:
                print("t67sb03 連線被拒絕。(略過)")
                continue
            finally:
                self.cli.closeConnection()
            parser2 = MopsHtmlParser_2(convert_charrefs=True)
            parser2.feed(res_t67sb03)
            p2_data = parser2.getP2Data()
            p1_data = aLine.split("|#|#|#|")
            xlsfile.addRowData((p1_data[2],
                                p1_data[1],
                                p2_data["B/S"],
                                p2_data["nof"],
                                p2_data["No. of U"],
                                "NA",
                                p2_data["Unit Price"],
                                p2_data["Total Amount"],
                                p2_data["comment"]))
        p1file.close()
        xlsfile.saveExcelFile()
        
    #註冊觀察進度者物件
    def registerProgressObserver(self, observer):
        self.progressObserver.append(observer)
        
        
        