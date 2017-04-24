# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:50:27 2017

@author: Administrator
"""

from numpy import *


def normalize(x,m1,m2):
    
    return (x-m2+pow(10,-100))/(m1-m2+pow(10,-100))
 
    
a = random.uniform(0,10,(10000,2))

b = [a[i][0]+a[i][1] for i in range(10000)]

     
max1 = max([a[i][0] for i in range(10000)])

min1 = min(a[i][0] for i in range(10000))

for i in range(10000):
    
    a[i][0] = normalize(a[i][0],max1,min1)

    
max2 = max([a[i][1] for i in range(10000)])

min2 = min([a[i][1] for i in range(10000)])

for i in range(10000):
    
    a[i][1] = normalize(a[i][1],max2,min2)

    
max3 = max(b)

min3 = min(b)

for i in range(10000):
    
    b[i] = normalize(b[i],max3,min3)

    
w = random.uniform(-1,1,(10,2))

v = random.uniform(-1,1,(10))

A = 0.05


def sigmoid(x):
    
    return 1/(1+pow(e,-x))

    
def feedback():
    
    for i in range(10000):
            
        O = [sigmoid(a[i][0]*w[j][0] + a[i][1]*w[j][1]) for j in range(10)]
             
        y = sum([O[k]*v[k] for k in range(10)])

        dv = b[i]-y
        
        for l in range(10):
            
            v[l] += A*dv*O[l]
        
        for m in range(2):
            
            for n in range(10):
                
                w[n][m] += A*O[n]*(1-O[n])*dv*v[n]*a[i][m]

    return w,v
 
    
def test(w,v,x,y):
    
    O = [sigmoid(x*w[j][0] + y*w[j][1]) for j in range(10)]
        
    y = sum([O[k]*v[k] for k in range(10)])
    
    return y

    
if __name__ == "__main__":
    
    w,v = feedback()
    
    f1 = open(r'C:\Users\Administrator\.spyder-py3\w1.txt','w')
    
    for i in range(10):
        
        for j in range(2):
            
            f1.write('%f ' % w[i][j])
            
        f1.write('\n')
        
    f1.close()
        
    f2 = open(r'C:\Users\Administrator\.spyder-py3\v1.txt','w')
    
    for i in range(10):
            
        f2.write('%f\n' % v[i])
        
    f2.close()
    
    x = input('x= ')
    
    y = input('y= ')
    
    x = normalize(float(x),max1,min1)
    
    y = normalize(float(y),max2,min2) 

    print(test(w,v,x,y)*20)  
    
      


 
        
        
        