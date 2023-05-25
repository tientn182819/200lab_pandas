import numpy as np 
import pandas as pd

#Dataframe là một mảng 2 chiều bao gồm hàng và cột như một spreadsheet hay sql. hoặc dataframe có thể có kết cấu từ a dict of Series và có thể có thành phần y như Series 

#CÁC CÁCH TẠO RA DATAFRAME

#1, từ dict of Series hoặc dict

a = {
    "one": pd.Series([1,2,3], index=["1","2","3"]),
    "two": pd.Series([4,5,6,7], index=["1","2","3","4"]),
    }

a1 = pd.DataFrame(a)
print(a1)

a2 = pd.DataFrame(a, index=["2","1","3"])
print(a2)

a3 = pd.DataFrame(a, index=["2","3","1"], columns=["two","one"])

print(a1.index)

print(a1.columns)

#2, From dict of ndarrays/list

b = {"one":[1,2,3,4,5], "two": [1,2,3,4,5]}
#Với narray hoặc list thì phải khai báo hai cột có độ dài bằng nhau nếu khống sẽ báo lỗi

b1 = pd.DataFrame(b)
print(b1)

#Gắn index
b2 = pd.DataFrame(b, index=["a", "b", "c", "d", "e"])
print(b2)

#Create from a list of a dictionary 
data2 = [{"a":1, "b":2}, {"a":5, "b":10, "c":20}]
print(pd.DataFrame(data2))
#Thuowfngd dược sử dụng cho file JSON

#Create from a list of Tuple
data3 = [('Peter1', 18,7),
         ('Peter2', 18,7),
         ('Peter3', 18,7),
         ('Peter4', 18,7),
         ('Peter5', 18,7)]

df3 = pd.DataFrame(data3, columns=['Name', 'Age', 'Score'])

print(df3)


