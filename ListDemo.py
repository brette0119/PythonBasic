#收集一堆資料list類別
#多筆資料初始化(可以收集異質類型)
names=["allen","barry","cathy","frank","deby","eric"]
print(type(names)) #問出類型
#問出集合參考物件數量
print(len(names)) #集合物件索引子 順序從零開始
print(names[0])
#指派給另一個變數 是否參考概念
names2=names; #複製參考位址 共同參考Reference
names[0]="angle"
print(names2)
#動態參考(List size是可以變動的)
names.append("green");
print(names)

#固定長度的集合 類似陣列
java=(60,90,100,50,70,60);
print(type(java)) #tuple
print(java[0]) #具有順序性 採用索引子
#java.appende("allen") 無法動態延展參考數量(固定數量)

#是否可以排序sort
names.sort(reverse=True) #tuple 無法sort reverse=True降冪排序
print(names)



