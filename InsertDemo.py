import pyodbc as odbc
#設定連接資料庫組態
server='localhost'
username='sa'
password='1111'
database='NORTHWND'
#連接上SQL(開啟一條連接)
connString='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';database='+database+';UID='+username+';PWD='+password
#開啟連接
connection=odbc.connect(connString)
#取得cursor
cursor=connection.cursor()
#採用整理一個Insert into SQL String SQL-Pass-Through 
sql="insert into Customers(CustomerID,CompanyName,Address,Phone,Country) values('{}',N'{}',N'{}','{}',N'{}')".format('E1001','巨匠東門','台南市東門路','060343434','中華民國')
#執行新增
cursor.execute(sql) #增刪修查詢都具有一個緩存
#正式交付Commit
connection.commit()
print('新增完成')


