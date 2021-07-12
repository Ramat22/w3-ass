# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:17:01 2021

@author: win10
"""
fruits= ["apple", "banana", "cherry"]
print(fruits[1]) 

fruits= ["apple", "banana", "cherry"]
if"apple" in fruits:
    print("yes,'apple' is in the fruits list")

fruits= ["apple", "banana", "cherry"]
fruits[1]="grapes" 
print(fruits) 

fruits= ["apple", "banana", "cherry"]
fruits[1:3]=["grapes"] 
print(fruits) 


fruits= ["apple", "banana", "cherry"]
fruits.append("grapes") 
print(fruits)   

fruits= ["apple", "banana", "cherry"]
fruits.insert(1,"grapes") 
print(fruits)   


fruits = ["apple", "banana", "cherry"]
print(fruits)


fruits = ["apple", "banana", "cherry"]
print(len(fruits))

fruit1=["grapes","papaya"]
fruit2=["banana","mango"]
fruits=fruit1+fruit2
print(fruits)
fruits = list(("apple", "banana", "cherry"))
print(fruits)


fruits = ["apple", "banana", "cherry", "cherry"]
print(fruits)


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


