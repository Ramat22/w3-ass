# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:04:43 2021

@author: win10
"""

set={"apple","banana","cherry"}
print("banana" in set)

set={"apple","cherry"}
for x in set:
    print(x)
    
set={"apple","banana","cherry"}
set.add("papaya")
print(set)

set={"apple","banana","cherry"}
tropical={"papaya","orange","mango"}
set.update(tropical)
print(set)

set={"apple","banana","cherry"}
set.remove("banana")
print(set)

set={"apple","banana","cherry"}
set.discard("banana")
print(set)

set={"apple","banana","cherry"}
x=set.pop()
print(x)
print(set)

set={"apple","banana","cherry"}
for x in set:
    print(x)
    
    
set1={"apple","banana"}
set2={1,2}
set1.update(set2)
print(set1)


