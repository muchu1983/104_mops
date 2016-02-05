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
        pass
        
    #收尾
    def tearDown(self):
        pass

    #測試XXX
    def test_xxx(self):
        logging.info("XXXXX")


#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


