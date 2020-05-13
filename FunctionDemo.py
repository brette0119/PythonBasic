#沒有參數沒有回應值function define
def helloWorld():
	print("Hello World")
	print("世界和平") #標準輸出Standard output
	

#function call
helloWorld()


#需要有參數的函數傳遞資訊
def helloTW(who,msg="世界和平"):
	result=who+' 說了...'+msg
	print(result)

#具有回應值Function
def helloEng(who):
	#類C#{} 字串Pattern 
	result="{} {}您好!!!".format(who,who)
	return result #直接下return　



helloTW("張三丰")
helloTW("張三丰","大家平安")

#呼叫具有參數與回應值的function
result=helloEng("eric")
print("結果 {}".format(result))