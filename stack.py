# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:25:01 2023

@author: sc26s
"""

def parenthesis(strs):
    res=[]
    close={"}":"{",")":"(", "]":"["}
    for c in strs:
        if c in close:    
            if res and res[-1]==close[c]:
                res.pop()
            else:
                return False
        else:
            res.append(c)
    return len(res)==0
"""
    if (len(strs)%2!=0):
        return False
    for i in strs:
        if(i=="(" or i=="{" or i=="["):
            res.append(i)
        else:
            if(len(res)==0):
                return False
            x=res.pop()
            if((x=="(" and i==")")or (x=="{" and i=="}") or (x=="["and i=="]")):
                continue
            else:
                return False
    return len(res)==0
"""
class MinStack(object):

    def __init__(self):
        self.st=[]
        self.mn=[]

    def push(self, val):
        
        self.st.append(val)
        if self.mn:
            self.mn.append(min(self.mn[-1], self.st[-1]))
        else:
            self.mn.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.st.pop()
        self.mn.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.st[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.mn[-1]
        """
        :rtype: int
        """
        
def evalRPN(self, tokens):
    s=[]
    for c in tokens:
        if c not in ['+','-',"*","/"]:
            s.append(int(c))
        else:
            a=s.pop()
            b=s.pop()
            if c=='+':
                s.append(a+b)
            elif c=='-':
                s.append(b-a)
            elif c=="*":
                s.append(a*b)
            else:
                s.append(int(float(b) / float(a)))
    return s.pop()
def generateParenthesis(self, n):        
    stack=[]
    res=[]
    def backtrack(openN, closeN):
        if(openN==closeN==n):
            res.append("".join(stack))
            return
        if openN<n:
            stack.append("(")
            backtrack(openN+1,closeN)
            stack.pop()
        if openN > closeN:
            stack.append(")")
            backtrack(openN, closeN+1)
            stack.pop()
    backtrack(0,0)
    return res
def temparature(nums):
    st=[]
    tp=[0]*len(nums)
    ind=[]
    for i in range(len(nums)):
        x=1
        while st and st[-1]<nums[i]:
           st.pop()
           x=ind.pop()
           tp[x]=i-x
        ind.append(i)
        st.append(nums[i])
    return tp

def carFleet(position,speed,target):
    pair=[[p,s]for p,s in zip(position,speed)]
    st=[]
    for p,s in sorted(pair)[::-1]:
        st.append((target-p)/s)
        if len(st)>=2 and st[-1]<= st[-2]:
            st.pop()
    return len(st)
def maxHeight(nums):
    st=[]
    mx=-1
    for i, n in enumerate(nums):
        if st and st[-1][1]>nums[i]:
            while st and st[-1][1]>nums[i]:
                j,x=st.pop()
                if (i-j)*x>mx:
                    mx=(i-j)*x
            st.append([j,nums[i]])
        else:
            st.append([i,nums[i]])
        while st:
            j,x=st.pop()
            if(len(nums)-j)*x>mx:
                mx=(len(nums)-j)*x
    return mx
            
            
            