


# --coding: utf-8 --

import unittest
from testcase1 import UserTestCase
from testcase2 import UserTestCase2


class VideoTestCase(unittest.TestCase):
	def setUp(self):
		print(" set up 开始")

	def tearDown(self):
		print("tear down 结束执行")

	def testCase1(self):
		print("VideoTestCase TestCase1")

	def testCase2(self):
		print("VideoTestCase TestCase2")
		self.assertEqual(1,1)


if __name__ == '__main__':
	# unittest.main()
	suite = unittest.TestSuite()

	loader = unittest.TestLoader()

	suite.addTests(loader.loadTestsFromTestCase(UserTestCase))
	suite.addTests(loader.loadTestsFromTestCase(UserTestCase2))


	runner = unittest.TextTestRunner(verbosity=2 )

	runner.run(suite)








