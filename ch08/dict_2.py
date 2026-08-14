dict1 = dict((('一月','正月'),('二月','花月')) )
print(dict1) 

dict2 = dict.fromkeys(('四月','五月'))
print(dict2)

dict2 = dict.fromkeys(['一月','四月'],'端月')
print(dict2)
print('dict1= ',dict1)
print(dict1.keys())
print(dict1.values())
print(tuple(dict1.values()))

print(dict1.items())
print(list(dict1.items()))

print(dict2.get('三月')) # 輸出結果 None
print('dict2= ',dict2)
dict2.setdefault('一月', '梅月')
print(dict2)

print(dict2.setdefault('三月', '梅月'))
print(dict1)

print(dict1.pop('10 月','沒有此值')) # NONE
print(dict1.pop('二月'))
print(dict2)
print(dict2.popitem()) 
print(dict2)
dict3 = {}

# print(dict3.popitem()) 

print('dict1= ',dict1)
print('dict2= ',dict2)
dict1.update(dict2)
print(dict1)

# dict1.clear()
del dict1
print(dict1)