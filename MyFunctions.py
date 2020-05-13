#沒有參數沒有回應值function define
def helloWorld():
	print("Hello World")
	print("世界和平") #標準輸出Standard output
	

#需要有參數的函數傳遞資訊
def helloTW(who,msg="世界和平"):
	result=who+' 說了...'+msg
	print(result)

#具有回應值Function
def helloEng(who):
	#類C#{} 字串Pattern 
	result="{} {}您好!!!".format(who,who)
	return result #直接下return　

