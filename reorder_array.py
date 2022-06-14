#this script reorder a array.
import random as rand
import math
r=rand.random()
def getRandomValue(limit):
    return math.floor((rand.random() * limit)%limit)

arr = [5 , 6, 9, 8 ,7 ,10 , 12]
l=len(arr)
for i in range(0,l):
    idx = getRandomValue(l)
    t = arr[i]
    arr[i]=arr[idx]
    arr[idx]=t

print(arr)
    
    
