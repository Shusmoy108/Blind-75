# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:27:33 2023

@author: sc26s
"""
from collections import Counter,deque
def maxProfit( nums):
    l=0
    r=1
    x=0
    while r<len(nums):
        if nums[l]>=nums[r]:
            l=r
        else:
            x=max(nums[r]-nums[l],x)
            
        r+=1
    return x

def longestSubstr(s):
    if len(s)<2:
        return len(s)
    l=0
    r=0
    x=0
    ch=set()
    while r<len(s):
        while s[r] in ch:
            ch.remove(s[l])
            l+=1
        ch.add(s[r])
        x=max(len(ch),x)
        r=r+1
    return x

def maxRepeatString(s,k):
    l=0
    r=0
    d={}
    x=0
    while r<len(s):
        if s[r] not in d.keys():
            d[s[r]]=1
        else:
            d[s[r]]+=1
        c=max(d.values())
        while  (r-l-c+1>k):
            d[s[l]]-=1
            l=l+1
        x=max(r-l+1,x)
        r=r+1
    return x

def stringPerm(s1,s2):
    l=0
    r=len(s1)
    while r<=len(s2):
      if Counter(s1)==Counter(s2[l:r]):
         return True
      l=l+1
      r=r+1
    return False
           
def mxwinsubstr(s,t):
    a=Counter(t)
    ans=""
    l=0
    r=0
    b={}
    x=0
    m=9999999999
    c=sum(a.values())
    while r<len(s):
        if s[r] in a.keys():
            b[s[r]]= 1 + b.get(s[r],0)
            if(b[s[r]]<=a[s[r]]):
                x+=1
        while x==c:
            print(x,c)
            print(l,r)
            if (r-l+1)<m:
                ans= s[l:r+1]
                m = r-l+1
            if s[l] in a.keys():
                b[s[l]]-=1
                if b[s[l]]<a[s[l]]:
                    x-=1   
            l=l+1
        r=r+1
    return ans

def maxslidewindow(nums,k):
    q=deque()
    ans=[]
    l=r=0
    while r<len(nums):
        while q and nums[q[-1]]<nums[r]:
            q.pop()
        q.append(r)
        if l>q[0]:
            q.popleft()
        if r+1>=k:
            ans.append(nums[q[0]])
            l=l+1
        r=r+1
    return ans

            