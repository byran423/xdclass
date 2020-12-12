import pymysql
from warnings import filterwarnings

filterwarnings("ignore", category=pymysql.Warning)


class MysqlDb:

	def __init__(self):
		self.conn = pymysql.connect('127.0.0.1', 'root', 'caifu123', 'xd_test')

		self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

	def __del__(self):

		self.cur.close()

		self.conn.close()

	def query(self, url, state='all'):
		self.cur.execute(url)

		if state == "all":
			data = self.cur.fetchall()
		else:
			data = self.cur.fetchone()
		return data



	def excute(self, url):
		try:
			rows = self.cur.execute(url)
			self.conn.commit()
			return rows
		except Exception as e:
			print("数据库错误{0}".format(e))
			print("master")
			self.conn.rollback()


if __name__ == '__main__':
	mydb = MysqlDb()
	r = mydb.query("select * from `case`")
	print(r)












