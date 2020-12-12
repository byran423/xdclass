


# --coding: utf-8 --

import unittest
from  testcase1 import  UserTestCase

class UserTestCase2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("setUpClass  开始")

	@classmethod
	def tearDownClass(cls):
		print("UserTestCase2 tear down 结束执行")

	def testCase1(self):
		print("UserTestCase2 TestCase1")

	def testCase2(self):
		print("UserTestCase2 TestCase2")
		self.assertEqual(1,1)

	def testCase3(self):
		print("UserTestCase2 TestCase3")


if __name__ == '__main__':
	#verbosity 默认为1 ，=0最简洁=2输出详细结果
    #unittest.main(verbosity=2)

	suite = unittest.TestSuite()

	# suite.addTest(UserTestCase2("testCase2"))
	# suite.addTest(UserTestCase2("testCase1"))
	# suite.addTest(UserTestCase("testCase1"))

	suite.addTests([UserTestCase2("testCase2"),UserTestCase2("testCase1")])


	run = unittest.TextTestRunner(verbosity=2)

	run.run(suite)










