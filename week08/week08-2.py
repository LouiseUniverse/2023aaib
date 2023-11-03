a=[1,3,5,7,9,11,13]  #數字範圍是死的
for i in range(7):
  print('第一個數字是', a[i])

N = len(a)     #數字範圍是活的
for i in range(N):
  print('第一個數字是',a[i])