# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import collections

def duplicate(nums):
    d=set() #hashset
    for i in nums:
        if i in d:
            return True
        d.add(i)
    return False

def anagram(s,t):
    #return Counter(s)==Counter(t)
    #return sorted(s)==sorted(t)
    d={}
    e={}
    for i in s:
        if i in d.keys():
            d[i]=d[i]+1
        else:
            d[i]=1
    for j in t:
        if i in e.keys():
            e[i]=e[i]+1
        else:
            e[i]=1
    for i in s:
        if d[i]==e.get(i,0):
            return False
    return True

def twoSum(nums, target):
    nums=list(nums)
    for i in range(len(nums)):
        j= target-nums[i]
        if j in nums and nums.index(j)!=i:
            return [i,nums.index(j)]
"""
    d={}
    for i, n in enumerate(nums):
        dif=target-n
        if dif in d:
            return [d[dif],i]
        d[n]=i
        """    

def groupAnagram(strs):
    d=collections.defaultdict(list)
    for i in strs:        
        c=[0] * 26
        for s in i:
            c[ord(s)-ord("a")]+=1
            d[tuple(c)].append(i)
        return d.values()

def kelement(nums,k):
    c={}
    f=[[] for i in range(len(nums)+1)]
    for i in nums:
        c[i]=1+c.get(i,0)
    for n,c in c.items():
        f[c].append(n)
    r=[]
    for i in f:
        for j in f[i]:
            r.append(j)
            if len(r)==k:
                return r
    
def productExceptSelf(nums):
    r=[1]*len(nums)
    pre=1
    for i in range(len(nums)):
        r[i]*=pre
        pre*=nums[i]
    post=1
    for i in range(len(nums)-1,-1,-1):
        r[i]*=post
        post*=nums[i]
    return r
    pre=[]
    post=[]
    for i in range(len(nums)):
        if(i==0):
            pre[i]=nums[i]
            post[len(nums)-1-i]=nums[len(nums)-1-i]
        else:
            pre[i]=pre[i-1]*nums[i]
            post[len(nums)-1-i]=post[len(nums)-i]*nums[len(nums)-1-i]
    r=[]
    for i in range(len(nums)-1):
        if(i==0):
            r.append(1*post[i+1])
        elif(i==len(nums)-1):
            r.append(pre[i-1]*1)
        else:
            r.append(pre[i-1]*post[i+1])
    return r

def sudoku(board):
    row=collections.defaultdict(set)
    col=collections.defaultdict(set)
    square=collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if(board[r][c]=='.'):
                continue
            if(board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]):
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            square[(r//3,c//3)].add(board[r][c])
    return True

def encode(strs):
    res=""
    for s in strs:
        res=res+str(len(s))+"#"+s
        
    return res

def decode(s):
    res=[]
    i=0
    while i< len(s):
        j=i
        while s[j]!='#':
            j+=1
        x=int(s[i:j])
        res.append(s[j+1:j+1+x])
       
        i=j+x+1
    return res

def longesSet(nums):
    d=set(nums)
    l=0
    for i in nums:
        if i-1 not in d:
            m=0
            while i+m in d:
                m=m+1
        l=max(m,l)
    return l

print(decode(encode(["neet","code"])))