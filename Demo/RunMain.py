
# --coding: utf-8 --

import unittest
import os

def load_all_case():
	"""加载指定路径全部测试用例"""
	#print(os.getcwd())
	case_path = os.path.join(os.getcwd(),"Usertest")
	#print(case_path)

	discover = unittest.defaultTestLoader.discover(case_path,pattern="*case.py",top_level_dir=None)
	print(discover)
	return  discover

if __name__ == '__main__':

	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(load_all_case())



















