a = list(map(int, input().split()))

ans = a[0] #取最前面的數字
for x in a: #把每個數字都循一次
  if x>ans: 
    ans = x #更新答案
print('最大值是:',ans) #離開迴圈就找到答案

for x in a:
  print(x)