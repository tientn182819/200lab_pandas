import numpy as np 
import pandas as pd

#Hàm concat thường chỉ được sử dụng để nối những file có cấu trúc giống nhau 
#Hàm merge thường để nối những cột với nhau 
#Dùng đê rgheps các bảng với nhau nếu như các bảng có cột chung

left = pd.DataFrame(
    {
        "key": ["K0","K1","K2","K3"],
        "A": ["A","B","C","D"],
        "B": ["A","B","C","D"],
        "C": ["A","B","C","D"]
    }
)

right = pd.DataFrame(
    {
        "key": ["K0","K1","K2","K3"],
        "D": ["A","B","C","D"],
        "E": ["A","B","C","D"],
        "F": ["A","B","C","D"]
    }
)

result = pd.merge(left, right,on="key") #on chỉ cột chung 
''' 
Nếu như tên cột không giống nhau có thể viêt snhuw sau 
pd.merge(left,right,"tên cột cần gộp ở bảng bên trái","tên cột cần gộp ở bảng bên phải")
'''

print('left: ',left)
print("right: ",right) 
print('result', result) 

'''
Nếu cột có nhiều bảng key có thể viết :
pd.merge= (left,right, how="left", on=["Cột key 1","cột key 2","Cột key ...." ])
với how là hình thức join : inner join, left join,...
'''

'''-------------------------------------------------------------------------------------------'''

left1 = pd.DataFrame(
    {
        "A": [1,2],
        "B": [3,4]
    }
)

right1 = pd.DataFrame(
    {
        "A": [4,5,6],
        "B": [2,2,2]
    }
)

'''Check for duplicates key'''
result = pd.merge(left, right, on="B", how="outer", validate="one_to_one")
#Khi dùng one to one nó sẽ check ở cột key xem có giá trị nào trùng nhau không, nếu trùng nhau nó sẽ báo lỗi

result2 = pd.merge(left, right, on = "B", indicator=True)
#Indicator dùng để so sash xem giá trị trong cột key theo bảng tham chiếu ở cột bên trái, phải hay cả hai