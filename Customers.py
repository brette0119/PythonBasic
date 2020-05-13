#定義一個類別
class Customers():
	#設計Data Field(Attribute)欄位 儲存資訊
	id=0  #這是一個整數 int class
	name='' #字串str class
	address=''
	phone=''
	#建構子Constructor (建構物件進行初始化Initializer)
	#第一個參數self 物件本體的意義(C# this) 參數採用預測值 表現建構子多載Overloading 
	def __init__(self,id=0,name='',address='',phone=''):
		self.id=id
		self.name=name
		self.address=address
		self.phone=phone

	
	#定義一個information (Instance Method-物件的方法)
	def information(self):
		msg='編號:'+str(self.id)+' 姓名:'+self.name
		return msg


#業務員類別 繼承Customers
class Sales(Customers):
	#attribute
	department='業務部'
	#自訂建構子
	def __init__(self, id=0, name='', address='', phone='',department=''):
		
		#父親的建構子部分可以呼叫
		super().__init__(id,name,address,phone)
		self.department=department
	#Overriding 覆寫
	def information(self):
		msg=super().information() #往父親的方法呼叫
		return msg+' 部門別:'+self.department

		