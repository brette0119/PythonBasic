#使用自訂類別
from MyCustomers import MyCustomers
#建構一個個體物件
customer1=MyCustomers('001','張三丰')
customer2=MyCustomers('002','張泰山')

print(customer1.information())
print(customer2.information())

