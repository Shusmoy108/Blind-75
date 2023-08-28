# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
        
                                                               
                                                             