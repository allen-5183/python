# 定義階乘函數 d(n)（使用遞迴 Recursive）
# 當 n <=l 時，回傳 1（基礎條件 Base Case，防止無限遞迴）。
# 當 n > 1 時，回傳 n*d(n-1)（遞迴呼叫，持續向下計算乘積）。
# 例如計算 d(5)：會推導為 5 X d(4)= 5*(4*d(3)) = 5 * 4 * (3*d(2)) = 5 * 4 * 3 * (2*d(1)) = 5 * 4 * 3 * 2 * 1。
def d(n):
   if n <= 1:
       return 1
   else :            # n > 1        
       return n * d(n-1) 
 
while True:
   n = eval(input('n = '))
   if (n >= 1):
       break
   else:
       print('輸入資料不符, 請重新輸入...')
 
fac = d(n)
print (f'{n}! = {fac}')