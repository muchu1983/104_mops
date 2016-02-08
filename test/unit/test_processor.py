"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
import unittest
import logging
from mops.processor import Processor

"""
測試 processor 模組
"""

class ProcessorTest(unittest.TestCase):

    #準備
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.psr = Processor()
        
    #收尾
    def tearDown(self):
        pass

    #測試 設定日期範圍
    def test_setDateRange(self):
        logging.info("ProcessorTest.test_setDateRange")
        self.assertTrue(self.psr.setDateRange("20150101", "20151231"))
        self.assertTrue(self.psr.setDateRange("20150201", "20150228"))
        self.assertFalse(self.psr.setDateRange("20150132", "20150229"))
        self.assertFalse(self.psr.setDateRange("20153112", "01012015"))
        
    #測試 parse p1_data.txt (一行)
    def test_parseP1DataLine(self):
        logging.info("ProcessorTest.test_parseP1DataLine")
        aLine = '5846|#|#|#|國泰人壽|#|#|#|104/01/07|#|#|#|國泰人壽公告處分Fidelity Funds-EU HY Bond Fund (USD)|#|#|#|document.fm_t67sb07.step.value="2";document.fm_t67sb07.co_id.value="5846";document.fm_t67sb07.DATE1.value="20150107";document.fm_t67sb07.SKEY.value="2";action="/mops/web/ajax_t67sb03";ajax1(this.form,"table01");|#|#|#|'
        #return == (co_id, DATE1, SKEY)
        self.assertEqual(("5846","20150107","2"), self.psr.parseP1DataLine(aLine))
        
    #測試 parse temp_data.txt
    def test_parseTempData(self):
        logging.info("ProcessorTest.test_parseTempData")
        self.psr.parseTempData()
        
    #測試 設定日期範圍
    def test_setDateRange(self):
        logging.info("ProcessorTest.test_setDateRange")
        self.psr.setDateRange("20160101", "20160207")
        self.assertEqual(self.psr.getDateRange()[0].year, 2016)
        self.assertEqual(self.psr.getDateRange()[0].month, 1)
        self.assertEqual(self.psr.getDateRange()[1].day, 7)
        
    #測試 執行抓取網頁與分析程序
    def test_process(self):
        self.psr.setDateRange("20150101", "20150110")
        self.psr.runProcess()

#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


