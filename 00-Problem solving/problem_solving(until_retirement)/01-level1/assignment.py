#Q1
num=int(input("enter an number:-"))
if num%2==0:
    print("enter number is even")
else:
    print("enter number is odd")


#Q2
num=int(input("enter first number:-"))
num1=int(input("enter second number:-"))
if num>num1:
    print(f"{num} is greater than {num1}")
else:
    print(f"{num1} is greater than {num}")


#Q3
num1=int(input("enter first number:-"))
num2=int(input("enter second number:-"))
num3=int(input("enter third number:-"))
if num1>num2 and num1>num3:
    print(f"{num} is greater ")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater ")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater")
else:
    print("all are equal")


#Q4
num=int(input("enter an number:-"))
if num==0:
    print("number is zero")
elif num>0:
    print("number is positive")
else:
    print("enter number is negative")

#Q5
age=int(input("enter your age:-"))
if age<0:
    print("enter an valid age")
else:
    if 0<=age<=12:
        print("child")
    elif 13<=age<=19:
        print("teenager")
    else:
        print("adult")

#Q6
marks=int(input('enter your marks:-'))
if marks<0 or marks>100:
    print("enter an valid mark")
else:
    if marks>=90:
        print("A")
    elif 80<=marks<=89:
        print("B")
    elif 70<=marks<=79:
        print("C")
    elif 60<=marks<=69:
        print("D")
    else:
        print("F")


#Q7
num=int(input("enter an number:-"))
if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")


#Q8
num=int(input("enter an number:-"))
if num%5==0 and num%3==0:
    print("divisible by 5 and 3")
else:
    print("not divisible by both")


#Q9
year=int(input("enter year:-"))
if year%4==0 or year%100==0:
    print("leap year")
else:
    print("not an leap year")


#Q10
num=int(input("enter an number:-"))
if 10<=num<=50:
    print("in range")
else:
    print("outof range")