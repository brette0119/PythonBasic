#測試繼承性
from Customers import Sales
from Customers import Customers
#建構業務員物件(建構子繼承來自於Customers)
sales1=Sales(100,'張三丰','高雄市','07-3434343')
print(sales1.department)
#建構業務員 自訂建構子
sales2=Sales(200,'張泰山','高雄市','07-3434343','第一業務部')
print(sales2.information())  #方法有繼承下來用

