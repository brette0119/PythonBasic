#變數定義 屬於強固型別 型態設定了不能變
myname="eric chen"  #使用資料指派時候直接推論型別出來
myaddress='高雄市' #Strong Type強型別
print(myaddress)

money=100;salary=100000 #沒有基本型別/屬於類別型別
myname=200000;
#釋放掉變數
del myname
#print(type(myname)) # type() 問型別 已經不存在了

#多變數一次定義
phone1,phone2='07-1234567','0922123456'
print(phone1,phone2)

