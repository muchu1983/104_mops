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

    #測試 t146sb10
    def test_request_t146sb10(self):
        logging.info("ClientTest.test_request_t146sb10")
        form_body = "encodeURIComponent=1&step=2&TYPEK=pub&co_id_1=&SDATE=20150101&EDATE=20151130&YEAR1=104&YEAR2=104&MONTH1=1&MONTH2=104&SDAY=1&EDAY=30&scope=2&sort=1&rpt=bool_t67sb07&firstin=1"
        ret = self.target.requestServer("t146sb10", form_body)
        tmpfile = open("res_t146sb10.html", "w+")
        tmpfile.write(ret)
        tmpfile.close()
        
    #測試 t67sb03
    def test_request_t67sb03(self):
        logging.info("ClientTest.test_request_t67sb03")
        form_body = "encodeURIComponent=1&step=2&TYPEK=pub&co_id=5846&DATE1=20150105&SKEY=1&firstin=1"
        ret = self.target.requestServer("t67sb03", form_body)
        tmpfile = open("res_t67sb03.html", "w+")
        tmpfile.write(ret)
        tmpfile.close()

#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


