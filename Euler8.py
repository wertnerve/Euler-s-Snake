eulerNumber= open("Euler8Number.txt","r")
charCount=0

curr=0
while curr is not 13:
    num1=eulerNumber.read(1)
    #num
    print(eulerNumber.read(1),end='')
    curr+=1

print(eulerNumber.read(-2))
print(eulerNumber.size())
    
