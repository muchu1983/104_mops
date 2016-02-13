"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
from datetime import datetime
from tkinter import Tk,Frame,Grid,Label,Button,Entry,StringVar
from mops.processor import Processor
from threading import Timer
"""
儀表板主畫面
"""

class Dashboard:
    
    #顯示儀表板
    def showup(self):
        self.psr = Processor()
        self.root = Tk()
        self.root.title("MOPS資訊觀測站")
        frame = Frame(self.root)
        frame.grid(row=0, column=0, sticky="news")
        self.stateV = StringVar()
        self.stateV.set("日期格式：yyyymmdd")
        self.statebarL = Label(frame, textvariable=self.stateV)
        sdateL = Label(frame, text="開始日期")
        edateL = Label(frame, text="迄止日期")
        self.sdateE = Entry(frame)
        self.edateE = Entry(frame)
        self.goBtn = Button(frame, text="確定", command=self.runProcess)
        self.statebarL.grid(row=0, column=0, rowspan=1, columnspan=3, sticky="news")
        sdateL.grid(row=1, column=0, rowspan=1, columnspan=1, sticky="news")
        edateL.grid(row=2, column=0, rowspan=1, columnspan=1, sticky="news")
        self.sdateE.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="news")
        self.edateE.grid(row=2, column=1, rowspan=1, columnspan=1, sticky="news")
        self.goBtn.grid(row=1, column=2, rowspan=2, columnspan=1, sticky="news")
        Grid.grid_rowconfigure(self.root, 0, weight=1)
        Grid.grid_columnconfigure(self.root, 0, weight=1)
        self.root.mainloop()
        
    #確定開始執行抓取資料
    def runProcess(self):
        self.goBtn.config(state="disabled")
        try:
            sdate = self.sdateE.get()
            edate = self.edateE.get()
            datetime.strptime(sdate, "%Y%m%d")
            datetime.strptime(edate, "%Y%m%d")
        except ValueError:
            self.stateV.set("日期格式錯誤，正確為：yyyymmdd")
            return None
        print("from " + sdate + " to " + edate)
        self.psr.setDateRange(sdate, edate)
        self.psr.registerProgressObserver(self) #observer 需實作 updateProgress
        t = Timer(0, self.psr.runProcess) #啟動另一個 thread 執行，畫面才不會「沒有回應」
        t.start()
        
    #進度更新
    def updateProgress(self, progress):
        self.stateV.set("進度：" + str(progress) + "%")
        if progress == 100:
            self.goBtn.config(state="normal")
            self.stateV.set("已完成。重新輸入日期：yyyymmdd")
        