"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
from datetime import datetime
from tkinter import Tk,Frame,Grid,Label,Button,Entry,StringVar
from mops.processor import Processor
"""
儀表板主畫面
"""

class Dashboard:
    
    def showup(self):
        root = Tk()
        frame = Frame(root)
        frame.grid(row=0, column=0, sticky="news")
        self.stateV = StringVar()
        self.stateV.set("日期格式：yyyymmdd")
        dateformatL = Label(frame, textvariable=self.stateV)
        sdateL = Label(frame, text="開始日期")
        edateL = Label(frame, text="迄止日期")
        self.sdateE = Entry(frame)
        self.edateE = Entry(frame)
        self.goBtn = Button(frame, text="確定", command=self.runProcess)
        dateformatL.grid(row=0, column=0, rowspan=1, columnspan=3, sticky="news")
        sdateL.grid(row=1, column=0, rowspan=1, columnspan=1, sticky="news")
        edateL.grid(row=2, column=0, rowspan=1, columnspan=1, sticky="news")
        self.sdateE.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="news")
        self.edateE.grid(row=2, column=1, rowspan=1, columnspan=1, sticky="news")
        self.goBtn.grid(row=1, column=2, rowspan=2, columnspan=1, sticky="news")
        Grid.grid_rowconfigure(root, 0, weight=1)
        Grid.grid_columnconfigure(root, 0, weight=1)
        root.mainloop()
        
    def runProcess(self):
        try:
            sdate = self.sdateE.get()
            edate = self.edateE.get()
            datetime.strptime(sdate, "%Y%m%d")
            datetime.strptime(edate, "%Y%m%d")
        except ValueError:
            self.stateV.set("日期格式錯誤，正確為：yyyymmdd")
            return None
        print("from " + sdate + " to " + edate)
        psr = Processor()
        psr.setDateRange(sdate, edate)
        psr.runProcess()