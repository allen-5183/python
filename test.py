g1=['林二','王一','張三','趙六','王一','李四','張三','陳五']
g2=['鄭十','趙六','劉千','廖八','柯七','張三','王一','呂九','柯七','蔡百']
s1 = set(g1)
print(s1)
print(len(s1))
print(f'熱門音樂社原來人數：{len(g1)}人  正確人數：{len(s1)}人')
s2 = set(g2)
print(f'流行音樂社原來人數：{len(g2)}人  正確人數：{len(s2)}人')
s3 =s1.intersection(s2)
print(f'重複參加社團名單：{s3}')

print(s1)
print(s2)
s4 =s1.union(s2)
print(f'合併後社團人數：{len(s4)}人')