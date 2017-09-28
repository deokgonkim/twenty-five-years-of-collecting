#! -*- coding=utf-8 -*-

#from mod_kbrr1.bit import to_binary
from mod_kbrr1.bit import to_bitmap

DEBUG = True

n = input("Enter number? ")

assert 1 <= n <= 16, "Number is out of range 1 - 16"

#print("Number %d is %s in Binary" % (n, to_binary(n)))
#print("Number %d is %s in Binary" % (n, to_bitmap(n, '#', ' ')))

arr1 = input("Enter arr1(Valid Python Expression)? ")

print(arr1)

arr2 = input("Enter arr2(Valid Python Expression)? ")

print(arr2)

#for i in arr1:
#    print(to_bitmap(i, '#', ' '))

for n1, n2 in zip(arr1, arr2):
    print(to_bitmap(n1 | n2, '#', ' '))
