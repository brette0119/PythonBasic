#查詢資料庫記錄之後封裝成DataFrame
import pyodbc as odbc
import pandas as pd

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
#需要對應每一欄收集清單list
cidlist=[]
company=[]
address=list()
phone=[]
country=[]
#while(if)  Conditional (result!=None) 
while result!=None:
	print('編號:%s 公司行號:%s 聯絡地址:%s 電話:%s 國家別:%s' %(result[0],result[1],result[2],result[3],result[4]))
	#使用集合物件收集相對欄位內容
	cidlist.append(result[0])
	company.append(result[1])
	address.append(result[2])
	phone.append(result[3])
	country.append(result[4])
	#繼續擷取下一筆
	result=cursor.fetchone()
#將多個集合物件list轉換成DataFrame
df=pd.DataFrame({'CustomerID':cidlist,'CompanyName':company,'Address':address,'Phone':phone,'Country':country})
print(df)
#DataFrame 查詢
dfCountry=df[df['Country']=='USA'] #df['Country']==value 產生dict
print(dfCountry)
#將DataFrame篩選國家別欄位 轉換成list
countryList=df['Country'].tolist();
print(countryList)
#重新封裝成一個DataFrame
dataCountry=pd.DataFrame({'Country':countryList,'id':countryList})
print(dataCountry)
#分組統計(每一個國家別有多少筆)
group=dataCountry.groupby(['Country']).agg(['count']) #count彙總函數操作
print(group)
#統計圖


connection.close()








