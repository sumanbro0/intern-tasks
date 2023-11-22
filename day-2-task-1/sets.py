#  Write a program that prompts the user to enter two sets of numbers. Print the
# intersection and union of the two sets

set1=set(input("Enter values for first set: eg. 1111\n"))
set2=set(input("Enter values for secoand set: eg. 1111\n"))
uni=set1.union(set2)
inter=set1.intersection(set2)
print(uni)
print(inter)