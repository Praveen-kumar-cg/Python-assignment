#A. Basic if
#Q=1
print("Output for question-1..............................................................")
x=19
if x>10:
    print("number is greatre than 10")


#Q=2
print("Output for question-2..............................................................")
age=18
if age>=18:
    print("Adult")

#Q=3
print("Output for question-3..............................................................")
num=float(input("enter an positive number:-"))
if num>0:
    print("enter number is positive.")

#Q=4
print("Output for question-4..............................................................")
marks=40
if marks>=40:
    print("pass")


#Q=5
print("Output for question-5..............................................................")
num=int(input("enter number:-"))
if num==0:
    print("enter number is zero")


#Q=6
print("Output for question-6..............................................................")
num=int(input("enter an number:-"))
if num>=0:
    print("enter number is positive")
else:
    print("enter number is negitive")


#Q=7
print("Output for question-7..............................................................")
age=int(input("enter your age:-"))
if age>=18:
    print("Adult")
else:
    print("minor")


#Q=8
print("Output for question-8..............................................................")
x=int(input("enter an number:-"))
if x%2==0:
    print("enter number is even")
else:
    print("enter number is odd")


#Q=9
print("Output for question-9..............................................................")
marks=int(input("enter your marks"))
if marks>=40:
    print("pass")
else:
    print("fail")


#Q=10
print("Output for question-10..............................................................")
x=int(input("enter your first number:-"))
y=int(input("enter your second number:-"))
if x>y:
    print("x is greater than y")
else:
    print("y is greater")

#Q=11
print("Output for question-11..............................................................")
marks=int(input("enter your marks:-"))
if marks>=90:
    print("A")
elif 75<marks<89:
    print("B")
elif 60<marks<74:
    print("C")
elif 40<marks<59:
    print("D")
else:
    print("F")

#Q=12
print("Output for question-12..............................................................")
num=int(input("enter an number:-"))
if num>0:
    print("enter number is positive")
elif num==0:
    print("enter number is zero")
else:
    print("enter number is negitive")

#Q=13
print("Output for question-13..............................................................")
a=int(input("enter your choise:-"))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
else:
    print("other")

#Q=14
print("Output for question-14..............................................................")
marks=int(input("enter your marks:-"))
if marks>=90:
    print("Excellent")
elif 60<marks<89:
    print("Good")
elif 40<marks<59:
    print("Pass")
else:
    print("Fail")

#Q=15
print("Output for question-15..............................................................")
a=int(input("enter your choise:-"))
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
else:
    print("other")

#Q=16
print("Output for question-16..............................................................")
age=int(input("enter your age:-"))
if age>=18:
    if age<=60:
        print("Between 18 and 60")
    else:
        print("greatre than 60")
else:
    print("minor")

#Q=17
print("Output for question-17..............................................................")
marks=int(input("enter your marks:-"))
if marks>=40:
    if marks>=75:
        print("Good")
    else:
        print("pass")
else:
    print("failed")

#Q=18
print("Output for question-18..............................................................")
a=int(input("Enter your number:-"))
if a>0:
    if a>100:
        print("Number is greatre than 100")
    else:
        print("Positive but less than 100")
else:
    print("zero or negative")


#Q=19
print("Output for question-19..............................................................")
age=int(input("enter your age:-"))
if age>=18:
    if age<=60:
        print("Between 18 and 60")
    else:
        print("greatre than 60")
else:
    print("minor")

#Q=20
print("Output for question-20..............................................................")
num = int(input("Enter a number: "))
if num != 0:
    if num > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
else:
    print("The number is zero.")

#Q=21
print("Output for question-21..............................................................")
age=int(input("enter your age:-"))
marks=int(input("enter your marks:-"))
if age>=18:
    if marks>=40:
        print("Eligible")
    else:
        print("marks are low but age fullfil")
else:
    print("not eligible..")


#Q=22
print("Output for question-22..............................................................")
num=int(input("enter number:-"))
if num<10:
    print("special number")
elif num>100:
        print("special number")
else:
    print("bitween 10 and 100 ")


#Q=23
print("Output for question-23..............................................................")
age=int(input("enter your age:-"))
has_id=input("enter True or False:-").capitalize()
if age>=18:
    if has_id=="True":
        print("Allowed!!!")
    else:
        print("id dont match")
else:
    print("not allowed???")


#Q=24
print("Output for question-24..............................................................")
x=int(input("enter 1st number:-"))
y=int(input("enter 2nd number:-"))
if x>10:
    if y>10:
        print("both are greatre than  10")
    else:
        print("y is less than 10")
elif x<=10:
    if y>10:
        print("x is less than 10 but y is greatre than 10")
    else:
        print("y is less than 10")
else:
    print("both are less than 10")

#Q=25
# print("Output for question-25..............................................................")
x=int(input("enter an number:-"))
if x<=0:
    if x==0:
        print("zero")
    else:
        print("negative number")
elif x>=100:
    if x==100:
        print("excect 100")
    else:
        print("number is greatre than 100")
else:
    print("number is bitween the 0 and 100")

#Q=26
print("Output for question-26..............................................................")
is_closed = False
if not is_closed: 
    print("Open")

#Q=27
print("Output for question-27..............................................................")
num=int(input("enter number:-"))
if num<50 and num>10:
    print("number is bitween 10 and 50")
else:
    print("other number")


#Q=28
print("Output for question-28..............................................................")
number = int(input("Enter a number: "))
if number < 10 or number > 50:
    print("Outside the range")
else:
    print("Inside the range")

#Q=29
print("Output for question-29..............................................................")
is_student=True
has_id=True
has_ticket=True
if is_student==True:
    if has_id==True:
        if is_student==True:
            print("allowed")
else:
    print("not allowed")


#Q=30
print("Output for question-30..............................................................")
age=int(input("enter your age:-"))
marks=int(input("enter your marks:-"))
has_id=True
if age>=18 and marks>40 and has_id==True:
    print("eligible")
else:
    print("not eligible")