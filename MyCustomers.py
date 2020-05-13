#定義一個Customers Class
#Name(paent class)
class MyCustomers(object):
	#建構子
	def __init__(self,id,name):
		#Data Field同時設定
		self.id=id
		self.name=name
	#Method 
	def information(self):
		return "編號:{} 姓名:{}".format(
			self.id,
			self.name
			)


