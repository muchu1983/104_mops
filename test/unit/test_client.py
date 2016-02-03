"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
import unittest
import logging
from mops.client import Client

"""
測試
"""

class ClientTest(unittest.TestCase):

    #準備
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.target = Client()
        
    #收尾
    def tearDown(self):
        self.target = None

    #測試XXX
    def test_requestServer(self):
        logging.info("ClientTest.test_requestServer")
        ret = self.target.requestServer()
        print(ret)


#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


