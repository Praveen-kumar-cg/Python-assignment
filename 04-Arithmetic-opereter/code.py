# Part 3 — Practical Programs
#Task 1 — Basic Arithmetic
num1=5
num2=4
print("Outpute for task-1:",num1+num2)
print("Outpute for task-1:",num1-num2)
print("Outpute for task-1:",num1*num2)
print("Outpute for task-1:",num1/num2)
print("Outpute for task-1:",num1//num2)
print("Outpute for task-1:",num1%num2)
print("Outpute for task-1:",num1**num2)

#Task 2 — Integer and Float
num1=10
num2=3.3
print("Outpute for task-2:",num1+num2,type(num1+num2))
print("Outpute for task-2:",num1-num2,type(num1-num2))
print("Outpute for task-2:",num1*num2,type(num1*num2))
print("Outpute for task-2:",num1/num2,type(num1/num2))
print("Outpute for task-2:",num1//num2,type(num1//num2))
print("Outpute for task-2:",num1%num2,type(num1%num2))
print("Outpute for task-2:",num1**num2,type(num1**num2))

#Task 3 — Student Marks
html=100
css=90
figma=99
x=html+css+figma
y=(html+css+figma)/3
print("Outpute for task-3:",x)
print("Outpute for task-3:",y)

#Task 4 — Product Calculation
price=200
quantity=20
total=price*quantity
print("Outpute for task-4:",total)

#Task 5 — Even or Odd
number = 10

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

#Task 6 — Division and Floor Division
num1=10
num2=3
num3=-3
print("Outpute for task-6:",num1/num2,type(num1/num2))
print("Outpute for task-6:",num1//num2,type(num1//num2))
print("Outpute for task-6:",num1/num3,type(num1/num3))
print("Outpute for task-6:",num1//num3,type(num1//num3))

#Task 7 — Negative Number Operations
num1=-5
num2=-4
print("Outpute for task-7:",num1+num2)
print("Outpute for task-7:",num1-num2)
print("Outpute for task-7:",num1*num2)
print("Outpute for task-7:",num1/num2)
print("Outpute for task-7:",num1//num2)
print("Outpute for task-7:",num1%num2)
print("Outpute for task-7:",num1**num2)

#Task 8 — Subtraction Edge Cases
num1=10
num2=20
num3=-10
num4=-20
print("Outpute for task-8:",num1-num2,num1-num3,num3-num1,num3-num4)

#Task 9 — Floor Division Edge Cases
num1=10
num2=3
num3=-10
num4=-3
print("Outpute for task-9:",num1//num2,num1//num4,num3//num2,num3//num4)

#Task 10 — Modulus Edge Cases
num1=10
num2=3
num3=-10
num4=-3
print("Outpute for task-10:",num1%num2,num1%num4,num3%num2,num3%num4)

#Part 4 — Operator Precedence
#Task 11
a=10 + 5 * 2
b=20 - 4 / 2
c=10 + 20 / 5 * 2
d=2 + 3 * 4 ** 2
e=100 - 20 // 5
print("Outpute for task-11:",a,b,c,d,e)

#Task 12 — Parentheses
a=10 + 5 * 2
b=(10 + 5) * 2
print("Outpute for task-12:",a,b)
c=20 - 10 / 2
d=(20 - 10) / 2
print("Outpute for task-12:",c,d)
e=2 + 3 * 4
f=(2 + 3) * 4
print("Outpute for task-12:",e,f)

#Part 5 — Boolean Arithmetic
#Task 13
num1=True
num2=False
print("Outpute for task-13:",num1+num2,type(num1+num2))
print("Outpute for task-13:",num1-num2,type(num1-num2))
print("Outpute for task-13:",num1*num2,type(num1*num2))
print("Outpute for task-13:",num2/num1,type(num2/num1))
print("Outpute for task-13:",num2//num1,type(num2//num1))
print("Outpute for task-13:",num2%num1,type(num2%num1))
print("Outpute for task-13:",num1**num2,type(num1**num2))

#Task 14
a=True + 5
b=False + 5
c=True * 10
d=False * 10
e=True - 5
f=False - 5
print("Outpute for task-14:",a,b,c,d,e,f)\

#Part 6 — String Operations
#Task 15
name="Praveen"
lname="kumar"
print("Outpute for task-15:",name+" "+lname)

#Task 16
name="Praveen"
lname="kumar"
print("Outpute for task-16:",(name+" "+lname)*4)

#Task 17
name="Praveen"
lname="kumar"
print("Outpute for task-17:",name+" "+lname,(name+" "+lname)*4)
print("The subtraction and division show the Type error.....")

#Part 7 — None Type
#Task 18
value = None
num=12
print("Outpute for task-18:"," Python show -TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'")

#Part 8 — Error Handling Practice
#Task 19
x=10000000
y=0
print("Outpute for task-19:","Python shows - ZeroDivisionError: division by zero")

#Task 20 — Mini Calculator
num1 = 10
num2 = 5

print("Outpute for task-20:","Addition: ...",num1 + num2)
print("Outpute for task-20:","Subtraction: ...",num1 - num2)
print("Outpute for task-20:","Multiplication: ...",num1 * num2)
print("Outpute for task-20:","Division: ...",num1 / num2)
print("Outpute for task-20:","Floor Division: ...",num1//num2)
print("Outpute for task-20:","Modulus: ...",num1%num2)
print("Outpute for task-20:","Exponentiation: ...",num1**num2)

#Part 10 — Final Challenge
#Task 21 — Arithmetic Expression Analyzer
a = 10
b = -3
c = 2.5
print("Outpute for task-21:")
print(a + b)
print(a - b)
print(a * c)
print(a / c)
print(a // b)
print(a % b)
print(a ** 2)
print((a + b) * c)
print(a + b * c)
print((a - b) / c)
print(a ** 2 + b * c)
print((a + c) // 2)