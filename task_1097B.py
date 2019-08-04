rtNumb = int(input())
rtList = []

for i in range(rtNumb):
	rtList.append(int(input()))

rtList.sort(reverse = True)
print(rtList)

if(sum(rtList) % 360 != 0):
	while(len(rtList) != 0):
		for i in range(len(rtList) - 1):
			if(rtList[0] >= rtList[i + 1]):
				rtList[0] -= rtList[i + 1]
				rtList[i + 1] = 0
		print("-after proc:", rtList)
		if(rtList[0] != 0):
			print("NO")
			exit(0)
		while(rtList.count(0) != 0):
			rtList.remove(0)
		print("--after drop:", rtList)
print("YES")
	
