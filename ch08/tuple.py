# 傳回元組內所有元素的總和
t1 = (10, 20, 30)  
print(sum(t1, 40)) # 100

# 傳回元組內元素最大者
print(max(t1))     # 30
# 傳回元組內元素最小者
print(min(t1))     # 10

# 將元組轉換成串列
list1 = [10, 20, 30]
print(tuple(list1)) # 輸出: (10, 20, 30)

# 將元組轉換成串列
tuple1 = (10, 20, 30, 20)
print(list(tuple1)) # 輸出: 串列 [10, 20, 30]

# 回傳元組的元素個數
print(len(tuple1)) # 輸出: 3

# 回傳元組中指定元素值的出現次數
print(tuple1.count(20)) # 輸出: 1

# 將元組中元素遞增排序後回傳，回傳值為串類型別 
tuple1 = (20, 10, 30)  
print(sorted(tuple1)) # 輸出: [10, 20, 30]
