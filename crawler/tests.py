from contextlib import AbstractContextManager
from typing import Any
from django.test import TestCase
from crawler import scrapers
import pandas

# Create your tests here.
class scrapers_TestCase(TestCase):
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        url = "https://currencyex.doitwell.tw/tw/"
        dfs = pandas.read_html(url)
        self.dfs = dfs

        pass
    
    def test_recommend(self):
        # Test
        test_df = self.dfs[0]
        test_df.columns=[u'種類','推薦','匯率','說明']
        test_df.drop([len(test_df)-1],inplace=True)

        # need to test
        df = scrapers.recommend()

        pandas.testing.assert_frame_equal(test_df,df)

    def test_all(self):
        # Test
        test_df = self.dfs[1]
        test_df.columns=['銀行名稱','銀行現金賣出','銀行現金買入','銀行即期賣出',"銀行即期買入","更新時間"]
        test_df.drop([len(test_df)-1],inplace=True)

        # need to test
        df = scrapers.all()
        
        pandas.testing.assert_frame_equal(test_df,df)
