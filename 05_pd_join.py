import numpy as np 
import pandas as pd

#Về bản chất JOIN chính là MERGE tuy có một số khác biệt 

left = pd.DataFrame(
    {
        "A":["A0","A1","A2"],
        "B":["B0","B1","B2"]
    },
    index=["K0","K1","K2"]
)

right = pd.DataFrame(
    {
        "C":["C0","C1","C2"],
        "D":["D0","D1","D2"]
    },
    index=["K0","K2","K3"]
)

result = left.join(right) 
#Khi dùng join nếu không đề cập gì thì cột tham chiếu chính là index

'''---------------------------------------------------------------'''

'''SỬ DỤNG JOIN VÀ MERGE VỚI INDEX'''

result2 = pd.merge(left, right, left_index=True, right_index=True, how="inner")

result3 = left.join(right,how="inner")