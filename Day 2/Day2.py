#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[7]:


#read text file, convert to int format in list
with open('input.txt') as fhand:
    line = [line.rstrip() for line in fhand]

entries = [int(i) for i in line]

print(entries)
print()
print ("# of values:", len(entries))


# In[8]:


#use itertools to create unique combos and check sum
count = 0
for a, b in itertools.combinations(entries, 2):
    count = count + 1
    print ((a, b), a+b)
    if a+b == 2020:
        print ("Found it:", a*b)
        answer = a*b


# In[9]:


print ("# of combos:", count)
print ("Answer:", answer)
