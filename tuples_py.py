# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:45:10 2021

@author: win10
"""

tuple=("apple","cherry")
print(tuple[1])

tuple=("apple","cherry")
print(tuple[1])

tuple=("apple","cherry")
print(tuple)

fruits=("apple","cherry")
(red,pink)=fruits
print(red)
print(pink)

fruits=("apple","cherry")
for x in fruits:
    print(x)
   
    
fruits=("apple","cherry")
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
    
fruits=("apple","cherry","banana")
thistuple = fruits*2
print(thistuple)

tuple1=("apple","cherry")    
tuple2=("banana","grapes")
tuple3=tuple1+tuple2
print(tuple3)