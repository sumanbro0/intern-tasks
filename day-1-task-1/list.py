# Write a program that takes N numbers as input from a user and puts them in a list. Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list and print them out. 

nums=[]
num_count=int(input("Enter num_count: "))
sum_of_odds=0
sum_of_evens=0


while(num_count>0):
    nums.append(int(input("Enter values: ")))
    num_count=num_count-1
print(nums)
for num in nums:
    if num%2==0:
        sum_of_evens+=num
    else:
        sum_of_odds+=num

print(f"sum of odds is {sum_of_odds} and sum of evens is {sum_of_evens}")



