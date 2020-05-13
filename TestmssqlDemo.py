import pymssql
#建立連接
conn=pymssql.connect(server='localhost',user='sa',password='1111',database='NORTHWND')
print(conn)
#透過連接取出cursor物件 as_dict 針對查詢結果 回應結果採用dict
cursor=conn.cursor(as_dict=True)
#查詢結果
sql="Select CustomerID,CompanyName,Address,Phone,Country from Customers"
cursor.execute(sql)
#取出第一筆
row=cursor.fecthone()
print(row)


