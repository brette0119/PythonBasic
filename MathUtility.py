#定義算術運算function
#合計不確定數量整數參數值*values 不確定參數數量 轉換成tuple(固定數量集合)
#動態參數 不確定數量 calAmt('消費金額',1,2,3,4.....) 1,2,3,4...轉換成tuple 固定參考數量的物件
def calAmt(type,*values):
	
	#合計
	total=0
	#foreach逐一參考出values參數內容
	for start in range(len(values)): #for start=0 to 4
		#累計值
		total+=values[start]


	return type+' 合計:'+str(total)

#處理每一季的業務金額 **配對名稱與值(dict),不確定數量
def calQuarSales(saleName,**values):
	keys=values.keys() #透過dict取出所有的key
	keyList=list(keys) #dict_key轉換成list ['Q1','Q2'] 才能使用順序問key
	for s in range(len(keys)):
		keyName=keyList[s] #採用配合順序去問到名稱
		value=values[keyName] # 使用keyName去問對應的值
		print('季別:{} 業績金額:{}'.format(keyName,value))
