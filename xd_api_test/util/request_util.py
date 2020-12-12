import requests


class RequestUtil:
	def __init__(self):
		pass

	def request(self, url, method, headers=None, param=None, content_type=None):
		"""
		通用请求工具类
		:param url:
		:param method:
		:param headers:
		:param param:
		:param content_type:
		:return:
		"""
		try:
			if method == "get":
				result = requests.get(url=url, headers=headers, params=param).json()
				return result
			elif method == "post":
				if content_type == "application/json":
					result = requests.post(url=url, json=param, headers=headers).json()
					return result
				else:
					result = requests.post(url=url, data=param, headers=headers).json()
					return result
			else:
				print("http method is not allowed!")


		except Exception as e:
			print("请求报错：{0}".format(e))

if __name__ == '__main__':
	# url = " https://api.xdclass.net/pub/api/v1/web/all_category"
	# r = RequestUtil()
	# response = r.request(url,'get')
	# print(response)

	url = "https://api.xdclass.net//pub/api/v1/web/web_login"
	r = RequestUtil()
	data = {"phone":"18668091423","pwd":"yb85119850"}
	headers = {"Content-Type":"application/x-www-form-urlencoded"}
	respons = r.request(url, 'post', headers=headers, param=data)
	print(respons)












