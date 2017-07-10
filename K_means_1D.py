#import required libraries

import numpy as np
from collections import Counter
import random

#comparing two lists for each and every element

def comp(list_1,list_2):
    l_1 = Counter(list_1)
    l_2 = Counter(list_2)
    return l_1 == l_2
   
print("K Means Algorithm for 1D array")
cluster1=[]
cluster2=[]
cluster1old=[]
cluster2old=[]
cluster1new=[]
cluster2new=[]
array=[2,4,10,12,3,20,30,11,25]
print(array)
k=2
m1=random.choice(array)
m2=random.choice(array)
i=2
print("1 Iteration")

#forming clusters for the first time
for x in array:
 p=x-m1
 q=x-m2
 if abs(p) < abs(q):
   cluster1.append(x)
 else:
   cluster2.append(x)
   
print("Mean 1 :",m1)
print("Mean 2 :",m2)  
print("Cluster 1 :",cluster1)
print("Cluster 2 :",cluster2)
cluster1new=cluster1[:]
cluster2new=cluster2[:]

# comparing the old cluster and the new cluster, if equal stop iterating

while not comp(cluster1old,cluster1new) and not comp(cluster2old,cluster2new) :
   cluster1old=cluster1new[:]
   cluster2old=cluster2new[:]
   mean1=np.mean(cluster1new)
   mean2=np.mean(cluster2new)
   del cluster1new[:]
   del cluster2new[:]
   for x in array:
     p=x-mean1
     q=x-mean2
     if abs(p) < abs(q):
       cluster1new.append(x)
     else:
       cluster2new.append(x)
   print(i,"Iteration")    
   print("Mean 1 :",mean1)
   print("Mean 2 :",mean2)  
   print("Cluster 1 :",cluster1new)
   print("Cluster 2 :",cluster2new)
   i=i+1
       
      
  
