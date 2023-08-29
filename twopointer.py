# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:27:22 2023

@author: sc26s
"""
def isPalindrome(self, s: str) -> bool:
    l=0
    r=len(s)-1
    while l<r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        elif not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
    return True
    s=s.lower()
    x=''
    for i in s:
        if (i>='a' and i<='z')or (i>='0' and i<='9'):
            x=x+i
    return x==x[::-1]

def twoSum(numbers, target):
    l=0
    r=len(numbers)-1
    while l<r:
        if numbers[l]+numbers[r]==target:
            return [l+1,r+1]
        elif numbers[l]+numbers[r]>target:
            r-=1
        else:
            l+=1

def threesum(nums):
    res=[]
    nums.sort()
    for i,n in enumerate(nums):
        if i>0 and n==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            ts=n+nums[l]+nums[r]
            if ts>0:
                r=r-1
            elif ts<0:
                l=l+1
            else:
                res.append([n,nums[l],nums[r]])
                l=l+1
                while nums[l]==nums[l-1] and l<r:
                    l=l+1
    return res

def mostWater(nums):
    mx=0
    l=0
    r= len(nums)-1
    while l<r:
        if(nums[l]>=nums[r]):
           
            area=(r-l)*nums[r]
            r-=1
        else:
            area=(r-l)*nums[l]
            l+=1
        mx=max(area,mx)
    return mx

def trapWater(nums):
    l=0
    x=0
    r=len(nums)-1
    maxL=nums[l]
    maxR=nums[r]
    while l<r:
        if(maxL<maxR):
            l+=1
            maxL=max(maxL,nums[l])
            x=x+ maxL-nums[l]
        else:
            r-=1
            maxR=max(maxR,nums[r])
            x=x+ maxR-nums[r]
        return x
    return x
    maxL=[0]*len(nums)
    maxR=[0]*len(nums)
    area=0
    for i in range(1,len(nums)):
        maxL[i]=max(max(maxL),nums[i-1])
        maxR[len(nums)-1-i]= max(max(maxR),nums[len(nums)-i])
    for i in range(len(nums)):
        x=min(maxL[i],maxR[i])-nums[i]
        if x>=0:
            area=area+x
    return area
        
                                                               
                                                             