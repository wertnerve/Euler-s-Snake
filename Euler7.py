#this program prints a list of prime numbers and its biggest value
primeList=[]

target=10000
curr=2
size=-1
while size<target:
    isPrime=True
    pTester=2
    while pTester<curr:
        if curr%pTester==0:
            isPrime=False
            break
        else : pTester+=1
    if(isPrime) :
        print(curr)
        primeList.append(curr)
        size+=1
    curr+=1
target+=1
print("The",target,"th prime number is",primeList.pop(size))
        
