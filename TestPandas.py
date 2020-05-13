#使用pandas package進行資料集處理
import pandas as pd
#設定list資料
id=[1,2,3,4,5,6,7,8,9,10]
name=['張三丰','張無忌','張泰山','張三','張翠珊','allen','barry','cathy','deby','eric']
address=['高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市']
#整理一個資料表(多行多列)
table =pd.DataFrame({'編號':id,'姓名':name,'地址':address})
print(table)

