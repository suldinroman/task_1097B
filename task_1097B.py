rotNumb = int(input())
rotList = []
resList = []

for i in range(rotNumb):
	rotList.append(int(input()))

resList.append(rotList[0])
for i in range(1, rotNumb):
	for j in range(len(resList)):
		resList[j] -= rotList[i]
		resList.append(resList[j] + 2 * rotList[i])

#for i in range(len(resList)):
#	resList.append(resList[i] * -1)

for i in resList:
	if(i % 360 == 0 or i == 0):
		print("YES")
		exit(0)
print("NO")
