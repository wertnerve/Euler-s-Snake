#the answer is 6857
#its the biggest prime factor
num=600851475143

factorTest=716151937
reverseFactorTest=num
rft=reverseFactorTest


factorList=[]
#factorList=[71, 839 ,1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633, 716151937]
print(factorList)


while factorTest<num:
    if factorTest==rft : break
    if num%factorTest==0:
        print('COUTNING UP, FOUND', factorTest)
        factorList.append(factorTest)
    factorTest+=1
    if num%rft==0 :
        print('COUNTING DOWN, FOUND',rft)
        factorList.append(rft)
    rft-=1
    if factorTest>1000000000:
        print(factorTest)
    


p=2
primeList=[]
size=-1
for x in factorList:
    isPrime=True
    while p<x:
        if x%p==0:
            isPrime=False
            #print(isPrime)
            break
        else : p+=1
    if(isPrime) :
        primeList.append(x)
        size+=1
    isPrime=True
    p=2
print('DONE')
print(primeList)
print('Largest prime factor :',primeList.pop(size))

            
        
