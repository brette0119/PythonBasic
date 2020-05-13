#測試動態不確定數量的參數
from MathUtility import calAmt
from MathUtility import calQuarSales

result=calAmt('消費金額',100,500,200,400,300)
print(result)

#傳遞配對內容 業務員季別銷售金額
calQuarSales('張三丰',Q1=100000,Q2=500000,Q3=800000,Q4=1000000)

