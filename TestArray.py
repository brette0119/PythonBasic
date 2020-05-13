#引用模組
import numpy as np
#設定陣列物件
data=[1,2,3]; #list
np1=np.array(data)
np2=np.array([5,6,7])
print(type(np1)) #numpy.ndarray
np3=np1+np2
print(np3)

#問陣列相關的資訊
print('元素型態:{}'.format(np1.dtype))
print('Shape:{}'.format(np1.shape))
print('陣列維度:{}'.format(np1.ndim))


