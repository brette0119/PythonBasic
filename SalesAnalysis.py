#銷售分析
import numpy as np
import matplotlib.pyplot as plot
#設定月分銷售金額list
month=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#月分銷售金額
sales=np.array([100,200,300,500,700,800,300,500,1200,1500,1400,900])
#繪製方塊圖
plot.bar(month,sales)
#設定XY軸的label
plot.xlabel('Month of 2019')
plot.ylabel('Money(million)')
#設定抬頭
plot.title('Sales for Month-2019')
plot.show()

