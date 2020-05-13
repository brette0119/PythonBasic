#測試自訂客戶類別物件
import Customers as cust
from Customers import Customers
#建構一個客戶物件
customers=cust.Customers(100,'張三丰','高雄市','07-3434343')
print(customers.information())

#直接使用類別建構子
customer2=Customers(200,'張無忌','台北市','02-3434434')
print(customer2.information())

#建構子多載Overloading (多載 可以採用不同的參數架構 建構物件)
customer3=Customers()
customer4=Customers(300,'張翠珊','台南市')
print(customer4.information())
