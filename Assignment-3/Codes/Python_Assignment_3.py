import random
toss = ['h','t']
noOfTrials = 10,000
a=0
b=0
c=0  
for i in range(1,10000):
  toss1 = random.choices(toss)
  toss2 = random.choices(toss)
  if(toss1 ==['h']):
      a=a+1
  if(toss2==['h']):
    b=b+1
  if((toss1==['h']) &(toss2==['h'])):
    c = c+1
    
PA = a/10000
PB = b/10000
PAB = c/10000
#PA.PB = PA*PB
print("PA = ",end = " ")
print(PA)
print("PB = ",end = " ")
print(PB)
print("PA.PB = ",end = " ")
print(PA*PB)
print("PAB = ",end = " ")
print(PAB)
