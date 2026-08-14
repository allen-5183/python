import random as R
# 生成 5 個 1 到 10 之間的隨機整數
for i in range(5):
    rnd = R.randint(1, 10)
    print(f'第 {i+1} 個亂數 : {rnd}')