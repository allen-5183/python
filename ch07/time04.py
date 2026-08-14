import time as T
t1 = T.time()
print(f'暫停前電腦時間:{t1}')
T.sleep(5)
t2 = T.time()
print(f'暫停後電腦時間:{t2}')
print(f'程式暫停了{t2-t1:.7f}秒')
# 暫停前電腦時間:1785739090.8115215