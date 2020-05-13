#測試import引用Modules
import MyFunctions as fun  #as 別名
from MyFunctions import helloTW
#使用別名呼叫function
fun.helloWorld()

#直接呼叫函數
result=helloTW("eric","世界和平")
print(result)
