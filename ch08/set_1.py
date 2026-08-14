set1 = {'Anastasia'} 
print (set1)

set1 = set('Anastasia')
print (set1)

set1 = set({'貓':'cat','狗':'dog'})
print(set1)

set1 = set('嘻嘻哈哈')
# 輸出: {'嘻', '哈'} (或 {'哈', '嘻'})
print(set1) 

set1.add('笑嘻嘻')
print(set1) # 輸出: {'嘻', '哈', '笑嘻嘻'} 

set1.remove('笑嘻嘻')
# 輸出: {'嘻', '哈'}
print(set1)

set1.discard('笑嘻嘻')
# set1.remove('笑嘻嘻')

set1.update('笑嘻嘻')
print(set1) # 輸出: {'嘻', '哈', '笑'} 

set1.pop()
print(set1) 