# Write a program that prompts the user to enter a number. Create a list of squares of all
# numbers from 1 to the user-entered number.

num=int(input("Enter a number: "))
squares=[]
for n in range(1,num+1):
    squares.append(n*n)
print(squares)