#importing libraries
import numpy as np
import pandas as pd
import math

#euclidean distance function
def eucledian_distance(p):
    global random_x,random_y
    return math.sqrt((random_x-p[0])**2+(random_y-p[1])**2)

n = int(input('Enter the number of points'))
df = pd.DataFrame()
x = []
y = []

for i in range(0, n):
    x.append(int(input('Enter x')))
    y.append(int(input('Enter y')))

df['x'] = x
df['y'] = y

# renaming cols
df.columns = ['x', 'y']

random_index = np.random.randint(0, len(df))
random_index1=np.random.randint(0,len(df))
print(random_index)
print(random_index1)
random_x, random_y = df.iloc[random_index]
rand_x,rand_y=df.iloc[random_index1]

df['ed'] = df[['x','y']].apply(eucledian_distance,axis=1)
df['ed'].head()
random_x=rand_x
random_y=rand_y
df['ed1'] = df[['x','y']].apply(eucledian_distance,axis=1)
df['ed1'].head()
print(df)

cluster_1 = pd.DataFrame(df[df['ed'] > df['ed1']][['x', 'y']])
cluster_2 = pd.DataFrame(df[df['ed'] < df['ed1']][['x', 'y']])

print("1 Iteration")
print("cluster1:")
print(cluster_1)
print("cluster2:")
print(cluster_2)

mean1_x=0
for i in range(0,len(cluster_1.index)):
    mean1_x=mean1_x+(cluster_1['x'].iloc[i])
mean1_x=mean1_x/len(cluster_1.index)
print(mean1_x)

mean1_y=0
for i in range(0,len(cluster_1.index)):
    mean1_y=mean1_y+(cluster_1['y'].iloc[i])
mean1_y=mean1_y/len(cluster_1.index)
print(mean1_y)

print("Mean 1:",mean1_x,mean1_y)

mean2_x=0
for i in range(0,len(cluster_2.index)):
    mean2_x=mean2_x+(cluster_2['x'].iloc[i])
mean2_x=mean2_x/len(cluster_2.index)
print(mean2_x)

mean2_y=0
for i in range(0,len(cluster_2.index)):
    mean2_y=mean2_y+(cluster_2['y'].iloc[i])
mean2_y=mean2_y/len(cluster_2.index)
print(mean2_y)

print("Mean 2:",mean2_x,mean2_y)

random_x=mean1_x
random_y=mean1_y
df['ed'] = df[['x','y']].apply(eucledian_distance,axis=1)
df['ed'].head()
random_x=mean2_x
random_y=mean2_y
df['ed1'] = df[['x','y']].apply(eucledian_distance,axis=1)
df['ed1'].head()
print(df)

cluster_1new = pd.DataFrame(df[df['ed'] > df['ed1']][['x', 'y']])
cluster_2new = pd.DataFrame(df[df['ed'] < df['ed1']][['x', 'y']])

print("2 Iteration")
print("cluster1:")
print(cluster_1new)
print("cluster2:")
print(cluster_2new)

cluster_1.loc['x', 'y'] = cluster_1new[['x', 'y']]
print(cluster_1)
'''
while cluster_1new != cluster_1:
    mean1_x = 0
    for i in range(0, len(cluster_1new.index)):
        mean1_x = mean1_x + (cluster_1new['x'].iloc[i])
    mean1_x = mean1_x / len(cluster_1new.index)
    print(mean1_x)

    mean1_y = 0
    for i in range(0, len(cluster_1new.index)):
        mean1_y = mean1_y + (cluster_1new['y'].iloc[i])
    mean1_y = mean1_y / len(cluster_1new.index)
    print(mean1_y)

    print("Mean 1:", mean1_x, mean1_y)

    mean2_x = 0
    for i in range(0, len(cluster_2new.index)):
        mean2_x = mean2_x + (cluster_2new['x'].iloc[i])
    mean2_x = mean2_x / len(cluster_2new.index)
    print(mean2_x)

    mean2_y = 0
    for i in range(0, len(cluster_2new.index)):
        mean2_y = mean2_y + (cluster_2new['y'].iloc[i])
    mean2_y = mean2_y / len(cluster_2new.index)
    print(mean2_y)

    print("Mean 2:", mean2_x, mean2_y)

    
    print(cluster_1)
'''



