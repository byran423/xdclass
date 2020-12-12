


# --coding: utf-8 --

import unittest


class UserTestCase(unittest.TestCase):
	def setUp(self):
		print(" set up 开始")

	def tearDown(self):
		print("tear down 结束执行")

	def testCase1(self):
		print("TestCase1")

	def testCase2(self):
		print("TestCase2")
		self.assertEqual(1,1)


if __name__ == '__main__':
	unittest.main()








