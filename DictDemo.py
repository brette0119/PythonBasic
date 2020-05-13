#資料辭典 採用多屬性對應設定 as JSON
person={"id":"001","name":"張三丰","address":"高雄市","country":"台灣"}
print(type(person))

print(person['id']) #Map 設定key Name
#走訪foreach 
for key in person:
	#相對key對應的值
	value=person[key]
	print('屬性名稱:{} 屬性值:{}'.format(key,value))

#取出所有的keys
keys=person.keys()
print(type(keys)) #dict_keys
print(keys)
#採用順序性走訪


for x in range(0,len(keys)):
	#採用順序問
	print(x)
	

