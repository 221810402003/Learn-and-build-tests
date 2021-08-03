#!/usr/bin/env python
# coding: utf-8

# In[18]:


str=input("Give an sentence without numbers: ")
n=str.split()
l=s=n[0]
for i in range(0,len(n)):
    if len(l)<len(n[i]):
        l=n[i]
    if len(s)>len(n[i]):
        s=n[i]
print("largest word is ",l)
print("smallest word is ",s)


# In[34]:


s=input("Enter a word: ")
k=int(input("No of places to shift: "))
q=""
for i in range(len(s)):
    val = ord(s[i])
    dup=k
        # if k-th ahead character exceed 'z'
    if val + k>122:
        k -= (122-val)
        k = k % 26
        q += chr(96 + k) 
    else:
        q += chr(val + k)    
    k = dup 
# print the new string
print (q)


# In[25]:


n=int(input())
for i in range(1, n + 1, 1):
    if (i == 1 or i == 0):
        continue;
    flag = 1;
    for j in range(2, ((i // 2) + 1), 1):
        if (i % j == 0):
            flag = 0;
            break;
    if (flag == 1):
        print(i, end = " ");

