import pandas as pd  
import numpy as np  

'''
Khởi tạo Series
Series là mảng 1 chiều có index, luôn luôn là 1 chiều phải có index( có thể tồn tại ở dạng số hoặc dạng chuỗi)
 s = pd.Series(data, index=index) 
 -  data có thể là python dict, an ndarray, a python lít, a scalar value 
 '''

s = pd.Series(np.random.randint(5), index = ["a", "b", "c", "d", "e"])
print(s)

#Khởi tạo bằng dictionary
d = {"a": 1, "b": 2, "c": 3}

print(pd.Series(d))

# thêm index từ một dictionary cho sẵn 
e = pd.Series(d, index=["b", "c","a","d"])
print(e)

# series sẽ luôn in index của pd.Series, sau đó so sánh với dictionary ban đầu để tìm ra index phù hợp, chỗ nào index k có giá trị sẽ để là NaN

#create from python list
a = [1,2,3]
print(pd.Series(a))
#Nếu không được truyền index thì giá trị index sẽ bắt đầu từ 0

#Create form scalar
print(pd.Series(5, index=["a","b","c","d","e"]))
#Sẽ xét số index và đưa ra các giá trị bằng với scalar truyền vào


'''----------------------------------------------------------------'''

'''So sánh String Index và Interger Index'''

#String Index 
series1 = pd.Series([1, 2, 3], index=['1','2','3'])
print(series1)
#Trong trường hợp này a['1'] = a[0]

#Interger Index
series2 = pd.Series([1, 2, 3], index=[1,2,3])
print(series2[1])
#Trường hợp này a[1] = 1 không có a[0]

#Pandas cũng có những tính chất tương tự như Numpy

# Có thể đặt tên cho Series bằng cách khai báo name="..."
s = pd.Series(np.random.randint(5), index=[1,2,3,4,5], name = "something")

# có thể rename bằng cách pandas.Series.rename
s2 = s.rename("sth different")
