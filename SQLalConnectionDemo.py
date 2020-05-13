#測試連接環境設定
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table,Column
#引用資料風格(不同資料庫風格不一樣)
from sqlalchemy.dialects.mssql import (NCHAR,NVARCHAR,MONEY)
#建立一個連接資料庫引擎物件(連接工廠 不會建立一條連接出來)
dbEngine=create_engine('mssql+pyodbc://sa:1111@DESKTOP-FTVU75K/NORTHWND?driver=SQL Server Native Client 11.0')
print(dbEngine)
#要一條連接(具有Open)
connection=dbEngine.connect()
print(connection) #sqlalchemy.engine.base.Connection

#建立MetaData 應對資料庫資料表Table Schema
customersMetaData=MetaData() #可以設定到兩個Table結構以上

#設定MetaData應對資料結構物件(Table)(table name->field Name attribute)
customersTB=Table('Customers',customersMetaData,
				  Column('CustomerID',NCHAR(5),nullable=False,primary_key=True),
				  Column('CompanyName',NVARCHAR(40),nullable=False),
				  Column('Address',NVARCHAR(60)),
				  Column('Country',NVARCHAR(15))
			 )
print(customersTB)

#準備一下建立前端Python具有虛擬物件導向資料庫(Persistence--持久層)
customersMetaData.create_all(dbEngine)
print(customersMetaData)
#操作新增作業(針對前端Python Persistence Table進行新增--同步更新到資料庫去)
#不會立即執行語法(Statement-SQL) 並非是直接新增一個物件(Entity class尚未設定)
ts=customersTB.insert().values(CustomerID='A8889',CompanyName='中華電信',Address='高雄市林森路',Country='中華民國')
print(ts) #尚未完成參數值設定
#Sync資料庫去正式維護
result=connection.execute(ts) #Connection 執行了Native SQL
print(result)
