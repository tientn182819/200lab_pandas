import numpy as np 
import pandas as pd

#Thường dùng để nối các hàng lại với nhau ( Các cột không đổi chỉ có số hàng tăng lên )

df1 = pd.DataFrame(
    {
    "A": [["1","2","3","4"]],
    "B": [["1","2","3","4"]],
    "C": [["1","2","3","4"]],
    "D": [["1","2","3","4"]],
    },
    index=[0,1,2,3],
)

df2 = pd.DataFrame(
    {
    "E": [["1","2","3","4"]],
    "F": [["1","2","3","4"]],
    "G": [["1","2","3","4"]],
    "H": [["1","2","3","4"]],
    },
    index=[2,3,4,5],
)

# df3 = pd.DataFrame(
#     {
#     "A": [["1","2","3","4"]],
#     "B": [["1","2","3","4"]],
#     "C": [["1","2","3","4"]],
#     "D": [["1","2","3","4"]],
#     },
#     index=[8,9,10,11],
# )

frames = [df1, df2]

result_axis0 = pd.concat(frames, axis=0)#Nối thêm hàng cột giữ nguyên 
'''pd.concat(objs, 
            axis = 0, : theo chiều dọc index, tức là theo hàng  
            join="outer",
            ignore_index = True,
            keys = None,
            levels = None,
            names = None,
            verify_intergrity=True
            copy = False)
'''
result_axis1 = pd.concat(frames, axis=1)#Nối thêm cột hàng giữu nguyên 
#Nhưng vì cấu trúc khác nhau : số cột khác nhau nên không d

result_innerjoin = pd.concat(frames, axis = 1, join = "inner")

# result_leftjoin = pd.concat(frames, axis = 1, join = "left")
result_reindex = pd.concat(frames, axis = 1).reindex(df1.index) 
#Reindex để đánh dấu dựa theo df1




print(result_axis0)

print(result_axis1) #Có thể dùng nhưng không nên dùng vì nó sẽ 


print(result_innerjoin)

# print(result_leftjoin)

#Thêm 1 Series vào Dataframe 

s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])

result_series = pd.concat([df1, s2.to_frame().T], ignore_index=True)

'''
- Vì s2 là Series tức là nó sẽ ở dạng cột 
- to_frame để chuyển series thành một dataframe 
- .T để xoay dataframe một góc 90 độ từ dọc thành ngang 
- ignore_index = true tức là tuân theo việc đánh index theo thứ tự của hệ thống, không liên qua đến index cũ
'''
 
