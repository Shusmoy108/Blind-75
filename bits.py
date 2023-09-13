# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:59:31 2023

@author: sc26s
"""

from collections import Counter

def singleNumber( nums):
    x= Counter(nums)
    for i in x.keys():
        if(x[i]==1):
            return i
def countBits (n):
    arr=[0]*(n+1)
    for i in range(n+1):
        arr[i]=arr[i//2]+i%2
    return arr

def hammingWeight(n):
    c=0
    while n>0:
        if n%2==1:
            c+=1
        n=n//2
    return c
   
def reverseBits(n):
    x=0
    for i in range(32):
        x=x+(n%2)*pow(2,31-i)
        n=n//2
    return x

def missingNumber(nums):
    x= min(nums)
    y= max(nums)
    if x>0:
        return 0
    for i in range(x,y+1):
        if i not in nums:
            return i
    return y+1

def getSum(a,b):
    return a+b

def reverse( x):
    m=1
    s=0
    print(pow(2,31)-1)
    if not (pow(-2,31)<=x and x <=(pow(2,31)-1)):
        return 0
    if x<0:
        m=-1
        x=-1*x
    while x>0:
        s=s*10+(x%10)
        x=x//10
    if not (pow(-2,31)<=s and s <=(pow(2,31)-1)):
        return 0
    return m*s