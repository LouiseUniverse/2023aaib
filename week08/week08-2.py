a=[1,3,5,7,9,11,13]  #數字範圍是死的
for i in range(4):
  print('第一個數字是', a[i])
print('上面數字範圍是死的 range(4)就只到第四個')
N = len(a)     #數字範圍是活的
for i in range(N):
  print('第一個數字是',a[i])