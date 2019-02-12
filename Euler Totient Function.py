k=2
primeList=[]
plSize=0
factorList=[]
size=-1
x=1

def setIsPrime(b):
    isPrime=b

number=int(input("Enter the number to have its Euler Phi factor determined! "))
while x<=number:
   if number%x!=0:
      primeList.append(x)   
   x+=1
print('DONE')
print("# of primes that precede",number,":",len(primeList))
print(primeList)
print("Totient=",len(primeList))
