#測試變數沒有預設值 該如何設定
myname=None #類似null 

print(type(myname)) #NoneType
#布林型別
ismar=False #True
print(ismar)
#物件位址
print(id(ismar)) #HashCode--內容一樣 數值會一樣

name1,name2='張三丰','張三丰'
print(id(name1),id(name2))
