"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
import xlwt
import os
from datetime import datetime
"""
excel 文件生成
"""
class XlwtWrapper:

    def __init__(self, filename=None):
        self.filename = filename
        style0 = xlwt.easyxf('font: name Times New Roman, bold on')
        self.wb = xlwt.Workbook(encoding="utf-8")
        self.ws = self.wb.add_sheet("mops sheet", cell_overwrite_ok=True)
        self.rowPointer = 0
        #加入標題
        self.ws.write(0, 0, "Date", style0)
        self.ws.write(0, 1, "Entity", style0)
        self.ws.write(0, 2, "Buy/Sell", style0)
        self.ws.write(0, 3, "Name of Fund", style0)
        self.ws.write(0, 4, "No. of Units", style0)
        self.ws.write(0, 5, "Currency", style0)
        self.ws.write(0, 6, "Unit Price", style0)
        self.ws.write(0, 7, "Total Amount", style0)
        self.ws.write(0, 8, "comment", style0)
    
    #加入資料
    def addRowData(self, rowdata):
        self.rowPointer = self.rowPointer+1
        col = 0
        for data in rowdata:
            self.ws.write(self.rowPointer, col, data)
            col = col+1
        
    #excel存檔
    def saveExcelFile(self):
        if self.filename == None:
            self.filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".xls"
        self.wb.save(self.filename)