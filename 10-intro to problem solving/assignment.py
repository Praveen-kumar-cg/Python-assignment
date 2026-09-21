# problem 1
#IPO model
# INPUT
#     First number
#     Second number

# PROCESSING
#     Add first number and second number

# OUTPUT
#     Sum of value

#Algorithm

# 1. Start
# 2. Read first number
# 3. Read second number
# 4. Add the two numbers
# 5. Display the result
# 6. Stop


a = int(input("Enter first number:-"))
b = int(input("Enter second number:-"))

sum_num = a + b
print(sum_num)

# Problem 2
#IPO model

# INPUT:
#  Take Number

# PROCESSING
# check the number%2
# if is 0 division Error

# output
# even or odd

#Algorithm

# start
# number%2 in Even
# number%2! in odd
# store the result
# display in result
# stop



num=int(input("enter an  number:"))
if num%2==0:
    print(" numbeer is even")
else:
    print("number is odd")

# Problem 3
#IPO model

# INPUT:
# take first number 
# take second number
# take three number

# PROCEESING:
# First>Second AND First>Tthird 
# compare numbers

# OUTPUT:
# largest number


#Algorithm

# Start.
# Input First, Second, Third.
# Compare all three.
# Print the largest.
# Stop.



first_num= int(input("Enter your first number: "))
second_num = int(input("Enter your second number: "))
third_num = int(input("Enter your third number: "))

if first_num > second_num and first_num > Third_num:
    print("Largest number is =", first_num)
elif second_num > first_num and second_num > Third_num:
    print("Largest number is =", second_num)
elif third_num>first_num and third_num>second_num:
    print("Largest =", Third_num)
else:
    print("all are equal ")


# Problem 4
#IPO model

# input
#  take Age

# Process	
# Check if age ≥ 18

# Output
# Eligible or Not Eligible

#Algorithm

# Start.
# Input age.
# If age is equal to 18, print Eligible.
# Otherwise print Not Eligible to vote.
# Stop.




age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Problem 5
#IPO model
# Input
# Price

# Process
# Apply 20% discount when  price ≥ 2000

# Output
# Final Price

#Algorithm

# Start.
# Input price.
# If price is minimum 2000:
# Discount = 20%.
# Final price = price − discount.
# Otherwise the  final price = price.
# Print final price.
# Stop.


price = float(input("Enter the  price: "))

if price >= 2000:
    price = price - (price * 20 / 100)

print("Final Price =", price)
	

# Problem 6
#IPO model

# Input
#  take Three subject marks

# Process
# Calculate the average

# Output
# Pass or Fail

#Algorithm

# Start.
# Input three marks.
# Calculate average.
# If average is equal 40, print Pass.
# Otherwise print the Fail.
# Stop.


marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

average_perc = (marks1 + marks2 + marks3) / 3

print("Average =", average_perc)

if average_perc >= 40:
    print("Pass")
else:
    print("Fail")