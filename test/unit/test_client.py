"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
import unittest
import logging
import codecs
from mops.client import Client
from mops.client import MopsHtmlParser_1
"""
測試
"""
class ClientTest(unittest.TestCase):

    #準備
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.cli = Client()
        self.parser1 = MopsHtmlParser_1(convert_charrefs=True)
        
    #收尾
    def tearDown(self):
        self.cli = None
        self.parser = None

    #測試 t146sb10
    def test_request_t146sb10(self):
        logging.info("ClientTest.test_request_t146sb10")
        form_body = "encodeURIComponent=1&step=2&TYPEK=pub&co_id_1=&SDATE=20150101&EDATE=20151130&YEAR1=104&YEAR2=104&MONTH1=1&MONTH2=104&SDAY=1&EDAY=30&scope=2&sort=1&rpt=bool_t67sb07&firstin=1"
        ret = self.cli.requestServer("t146sb10", form_body)
        tmpfile = codecs.open("res_t146sb10.html", "w+", "utf-8")
        tmpfile.write(ret)
        tmpfile.close()
        
    #測試 t67sb03
    def test_request_t67sb03(self):
        logging.info("ClientTest.test_request_t67sb03")
        form_body = "encodeURIComponent=1&step=2&TYPEK=pub&co_id=5846&DATE1=20150105&SKEY=1&firstin=1"
        ret = self.cli.requestServer("t67sb03", form_body)
        tmpfile = codecs.open("res_t67sb03.html", "w+", "utf-8")
        tmpfile.write(ret)
        tmpfile.close()
        
    #測試 parser
    def test_html_parser(self):
        logging.info("ClientTest.test_html_parser")
        form_body = "encodeURIComponent=1&step=2&TYPEK=pub&co_id_1=&SDATE=20150101&EDATE=20151231&YEAR1=104&YEAR2=104&MONTH1=1&MONTH2=104&SDAY=1&EDAY=31&scope=2&sort=1&rpt=bool_t67sb07&firstin=1"
        htmldata = self.cli.requestServer("t146sb10", form_body)
        self.parser1.feed(htmldata)
        

#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


