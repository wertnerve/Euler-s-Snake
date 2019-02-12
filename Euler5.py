
curr=1
nums=[]
while(curr<=20):
    nums.append(curr)
    curr+=1
curr=0
evenlyDivides=False
while(evenlyDivides!=True):
     curr+=1
     for x in nums:
         evenlyDivides=True
         if(curr%x>0):
             #print(curr, 'failed when divided by', x)
             evenlyDivides=False
             break
         
     
     
print(curr)
