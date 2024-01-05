
#1
#a=list(map(int,input().split()))
#ans=sum(a)
#for num in a:
#	if num<0: ans=ans-num
#print(ans,end='')

#2
a=list(map(int,input().split()))
ans = 0
for b in a:
	if b>0: ans += b
print(ans, end='')