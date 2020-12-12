# coding: utf-8

import unittest
from util.request_util import RequestUtil

host = "https://api.xdclass.net"


# noinspection PyArgumentList
class IndexTestCase(unittest.TestCase):


	def testIndexCategoryList(self):
		"""
		首页分类列表
		"""
		request = RequestUtil()
		url = host + "/pub/api/v1/web/all_category"
		response = request.request(url, "get")
		self.assertEqual(response['code'], 0, "业务状态不正常")

		self.assertTrue(len(response["data"]) > 0, "分类列表为空")


if __name__ == '__main__':
	unittest.main()










