#函數堆疊呼喚
def hello(func):  #function point 
	print("您好")# 原始function委派進行擴充執行功能
	return func

#呼喚這一個process被委派到hello()裡面去

def process():
	print("程序處理中...")

#Delegate委派功能到目標去 包裝起來回應一個function
#執行階段產生的function
newProcess=hello(process);

#一個程序呼叫兩個程序
newProcess()

#擴充原始的decProcess功能(前置作業有先執行hello function外掛的程序)
@hello
def decProcess():
	print("封裝程序處理....")


decProcess()




