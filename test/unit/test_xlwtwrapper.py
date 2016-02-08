"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
import unittest
import logging
import time
from mops.xlwtwrapper import XlwtWrapper

"""
測試 excel 寫入
"""

class XlwtWrapperTest(unittest.TestCase):

    #準備
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        pass
        
    #收尾
    def tearDown(self):
        pass

    #測試建立檔案
    def test_initial(self):
        logging.info("XlwtWrapperTest.test_initial")
        wrapper = XlwtWrapper()
        wrapper.saveExcelFile()
    
    #測試寫入行資料
    def test_addRowData(self):
        logging.info("XlwtWrapperTest.test_addRowData")
        wrapper = XlwtWrapper()
        wrapper.addRowData(("20160208", "ABC", "B", "DEF", "123", "TWD", "456", "789", "DEF"))
        wrapper.saveExcelFile()


#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


