a = int(input())

total = 0
for i in range(1,1000):
	total += i
	if total > a:
		ans = i
		break
print(ans,end='')