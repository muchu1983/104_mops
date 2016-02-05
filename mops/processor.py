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

class Processor:
    
    #建構子
    def __init__(self):
        self.fromDate = ""
        self.toDate = ""
    
    #設定並檢查日期
    def setDateRange(self, fromDate, toDate):
        try:
            datetime.strptime(fromDate, "%Y%m%d")
            datetime.strptime(toDate, "%Y%m%d")
        except ValueError:
            print("日期格式錯誤，正確是：yyyymmdd")
            return False
        print("日期格式正確 from %s to %s" % (fromDate, toDate))
        return True
        
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
        