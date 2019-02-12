numList=[]
i=1
while i<1000:
    if i%3 == 0:
        numList.append(i)
    elif i%5 == 0:
        numList.append(i)
    i+=1
print(numList)
sum=0
for i in numList:
    sum+=i
print(sum)
