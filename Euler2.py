fibList=[1]
previous=1
secondPrevious=1

p=previous
sp=secondPrevious


num=0
while num < 4000000:
 num=p+sp
 fibList.append(num)
 sp=p
 p=num
 

#print(fibList)


sum=0
for i in fibList:
    if i%2==0 : sum+=i
print()
print(sum)
