datas = {'A001':['汽水',25],
        'A005':['公主麵',10],
        'A006':['口香糖',8],
        'A003':['冰棒',20]}

num=input('請輸入貨號：')

if num not in datas:
    print(f'貨號：{num} 不存在')
    name=input('請輸入品名：')
    money=int(input('請輸入售價：'))
    datas[num]=[name,money]

d = datas.get(num)


print (d)
print(f'貨號：{num} 品名：{d[0]} 售價：{d[1]}元')
