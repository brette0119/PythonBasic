#連接MSSQL 採用ODBC
import pyodbc as odbc
#設定連接資料庫組態
server='localhost'
username='sa'
password='1111'
database='NORTHWND'
driver='{ODBC Driver 17 for SQL Server}'
#連接上SQL(開啟一條連接)
connString='DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(driver,server,database,username,password)

connection=odbc.connect(connString)
print(type(connection)) #pyodbc.Connection
#產生一個Cursor物件(類似命令物件) 必須與Connection物件互動
cursor=connection.cursor()
print(type(cursor)) #pyodbc.Cursor
#透過cursor物件下命令SQL-Pass-Through
cursor.execute("Select CustomerID,CompanyName,Address,Phone,Country from Customers") #執行命令同時產一個SQL ResultSet cursor物件直接應對 逐筆擷取Fetching
#進行(On-line)逐筆讀取Fetching 
result=cursor.fetchone() #紀錄指標移動到下一筆
print(result[0]) #pyodbc.Row
#while(if)  Conditional (result!=None) 
while result!=None:
	print('編號:%s 公司行號:%s 聯絡地址:%s 電話:%s 國家別:%s' %(result[0],result[1],result[2],result[3],result[4]))
	#繼續擷取下一筆
	result=cursor.fetchone()
connection.close()







