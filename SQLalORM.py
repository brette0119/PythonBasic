#測試連接環境設定
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table,Column
#引用資料風格(不同資料庫風格不一樣)
from sqlalchemy.dialects.mssql import (NCHAR,NVARCHAR,MONEY)
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#建立一個連接資料庫引擎物件(連接工廠 不會建立一條連接出來)
dbEngine=create_engine('mssql+pyodbc://sa:1111@DESKTOP-FTVU75K/NORTHWND?driver=SQL Server Native Client 11.0')
print(dbEngine)
#要一條連接(具有Open)
connection=dbEngine.connect()
print(connection) #sqlalchemy.engine.base.Connection

#建立MetaData 應對資料庫資料表Table Schema
customersMetaData=MetaData() #可以設定到兩個Table結構以上

#ORM(R-Rlational Table結構描述)
#設定MetaData應對資料結構物件(Table)(table name->field Name attribute)
customersTB=Table('Customers',customersMetaData,
				  Column('CustomerID',NCHAR(5),nullable=False,primary_key=True),
				  Column('CompanyName',NVARCHAR(40),nullable=False),
				  Column('Address',NVARCHAR(60)),
				  Column('Country',NVARCHAR(15))
			 )
print(customersTB)

#規劃一個Entity Class 應對資料表結構MetaData
#ORM (O-Object 類別規劃)
class Customers(object):
	#自訂建構子
	def __init__(self,CustomerID,CompanyName,Address,Country):
		#設定Attribute指派相對參數內容
		self.CustomerID=CustomerID
		self.CompanyName=CompanyName
		self.Address=Address
		self.Country=Country

#Mapping(ORM-M)
mapper(Customers,customersTB) #Entity->Table Mapping
#連接資料庫綁定結構(採用一個Global綁定後端資料庫架構)
base=declarative_base()
base.metadata.create_all(dbEngine)

#透過資料庫引擎 能夠建立一條Session(交談) 透過一個Session 工廠
Session =sessionmaker()
print(Session)
#將這一個Session工廠與資料庫引擎綁在一起(透過工廠建立一條條Session執行資料維護)Criteria (基準)
#綁定引擎上面
Session.configure(bind=dbEngine)
#要一條Seession(Criteria)
session=Session()
print(session) #sqlalchemy.orm.session.Session
#使用Session操作資料維護(Criteria)
result=session.query(Customers).filter(Customers.Country=='UK').all()
print(type(result)) #list物件
#走訪每一個Customers物件
for row in result:
	print('編號:{} 公司行號:{} 地址:{} 國家:{}'.format(row.CustomerID,
										  row.CompanyName,
										  row.Address,
										  row.Country))
