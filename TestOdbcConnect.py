#連接MSSQL 採用ODBC
import pyodbc as odbc
#設定連接資料庫組態
server='localhost'
username='sa'
password='1111'
database='NORTHWND'
#連接上SQL(開啟一條連接)
connString='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';database='+database+';UID='+username+';PWD='+password

connection=odbc.connect(connString)
print(type(connection)) #pyodbc.Connection

