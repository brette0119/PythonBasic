#DataFrame資料進行繪製
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
#隨機碼產生
data=np.random.randn(50,3) #產生兩個維度 [20,3]
print(type(data)) #ndarray(維度類別)
print(np.arange(20))
#ndarray 轉換成DataFrame(ndarray,arange,columns)
pd.DataFrame()
df=pd.DataFrame(index=np.arange(50),data=data,columns=['A','B','C'])
print(df)
#df.cumsum() 針對NaN轉換可以進行處理
df.plot()
plot.show()
