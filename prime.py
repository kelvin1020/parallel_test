#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import decimal as dcm
import time
import numpy as np

def primef(n):
    if n<1:
        return #如果n小于1, 返回None
    if n==1:
        return 2 #第一个质数是2
    else:
        loop = 1
        a = primef(n-1) + 1 #开始从已有质数起使用筛法
        while loop:
            for b in range(1,n-1+1):
                c = a%primef(b)#分别除以前边的质数
                if not c:        #若有被整除的，被除数 +1, 重新开始循环
                    a += 1
                    break      
                if b == n-1:     #如果所有之前的质数都除不尽，返回被除数
                    loop = 0
                    return a                

def calPrime(n):
    beginn = time.time()
    a = primef(n)   
    endd = time.time()
    b = endd - beginn
    return a, b


ta = time.time()
n = 10

for i in range(1, n):
    with open("prime.txt", "a") as f:
        print(calPrime(i), file = f)

tb = time.time()
with open("prime.txt", "a") as f:
        print("#The program costs %4.2fs"%(tb - ta), file = f)

