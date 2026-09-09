#1. Positive, Negative, or Zero
print("Output for question-1..............................................................")
num=int(input("Enter an number:-"))
if num>0:
    print("Enter number is positive!!")
elif num==0:
    print("Enter number is zero!!")
else:
    print("enter number is negative")


#2. Even or Odd + Positive or Negative
print("Output for question-2..............................................................")
num=int(input("enter an number:-"))
if num>0 and num%2==0:
    print("Positive even")
elif num>0 and num%2!=0:\
    print("Positive Odd")
elif num<0 and num%2==0:
    print("Negative even")
elif num<0 and num%2!=0:
    print("Negative Odd")
else:
    print("zero")

#3. Largest of Two Numbers
print("Output for question-3..............................................................")
num1=int(input("Enter first number:-"))
num2=int(input("Enter second number:-"))
if num1>num2:
    print("num1 is larger than num2")
elif num1<num2:
    print("num2 is larger than num1")
else:
    print("both are equal")


#4. Smallest of Three Numbers
print("Output for question-4..............................................................")
num1=int(input("Enter first number:-"))
num2=int(input("Enter second number:-"))
num3=int(input("Enter third number:-"))
if num1>num2 and num1>num3:
    if num2>num3:
        print("num3<num2<num1")
    else:
        print("num2<num3<num1")
elif num2>num1 and num2>num3:
    if num1>num3:
        print("num3<num1<num2")
    else:
        print("num1<num3<num2")
elif num3>num1 and num3>num2:
    if num1>num2:
        print("num2<num1<num3")
    else:
        print("num1<num2<num3")
else:
    print("all are equal")


#5. Largest of Three Numbers
print("Output for question-5..............................................................")
num1=int(input("Enter first number:-"))
num2=int(input("Enter second number:-"))
num3=int(input("Enter third number:-"))
if num1>num2 and num1>num3:
    print(num1,"is the largest")
elif num2>num1 and num2>num3:
    print(num2,"is the largest")
elif num3>num1 and num3>num2:
    print(num3,"is the largest")
else:
    print("all are equal")



#6. Divisible by 5 and 11
print("Output for question-6..............................................................")
num=int(input("Enter an number:-"))
if num%5==0 and num%11==0:
    print("Divisible by both 5 and 11")
elif num%5==0 and num%11!=0:
    print("Divisible only by 5")
elif num%5!=0 and num%11==0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")


#7. Divisible by Either 3 or 7
print("Output for question-7..............................................................")
num=int(input("Enter an number:-"))
if num%3==0 and num%7==0:
    print("Divisible by both 3 and 7")
elif num%3==0 and num%7!=0:
    print("Divisible only by 3")
elif num%3!=0 and num%7==0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")


#8. Pass or Fail
print("Output for question-8..............................................................")
num=int(input("Enetr an number:-"))
if num>100 or num<0:
    print("invalid marks!!!")
else:
    if num<40:
        print("Fail")
    else:
        print("Pass")


#9. Grade Calculator
print("Output for question-9..............................................................")
marks=int(input("enter your marks:-"))
if marks>100 or marks<0:
    print("enter valid marks!!!") 
else:
    if marks>=90:
        print("A")
    elif 80<marks<=89:
        print("B")
    elif 70<marks<=79:
        print("C")
    elif 60<marks<=69:
        print("D")
    elif 40<=marks<=59:
        print("E")
    else:
        print("Fail")


#10. Voting Eligibility
print("Output for question-10..............................................................")
age=int(input("enter your age:-"))
if age>120:
    print("unrealstic age")
elif age<0:
    print("Invalid age")
elif age<18 and age>=0:
    print("Cannot vote")
else:
    print("Can vote")


#11. Leap Year
print("Output for question-11..............................................................")
year=int(input("enter an leap number:"))
if year%400==0:
    print("leap year")
elif year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not leap year")

#12. Character Type
print("Output for question-12..............................................................")
char=input("enter an character type:-").strip()
if ord(char)>=65 and ord(char)<=91:
    print("uppercase ")
elif ord(char)>=97 and ord(char)<=123:
    print("lowercase ")
elif ord(char)>=48 and ord(char)<=57:
    print("digit")
else:
    print("special character")

#13. Vowel or Consonant
print("Output for Question 13.................................................")
char=input("Enter an single character:")
if ord(char)==97 or ord(char)==101 or ord(char)==105 or ord(char)==111 or ord(char)==117 or ord(char)==65 or ord(char)==69 or ord(char)==73 or ord(char)==79 or ord(char)==85:
    print("Vowel")
elif ord(char)>=48 and ord(char)<=57:
    print("Invalid input")     
elif ord(char)!=97 or ord(char)!=101 or ord(char)!=105 or ord(char)!=111 or ord(char)!=117 or ord(char)!=65 or ord(char)!=69 or ord(char)!=73 or ord(char)!=79 or ord(char)!=85 :
    print("Consonant")


#14. Profit or Loss
print("Output for Question 14.................................................")
cost_price=float(input("enter cost price:-"))
selling_price=float(input("enter selling price:-"))
if cost_price<selling_price:
    print("profit=",(selling_price-cost_price))
elif cost_price>selling_price:
    print("loss=",(selling_price-cost_price))
else:
    print("no profit no loss...")


#15. Profit/Loss Percentage
print("Output for Question 15.................................................")
cost_price=float(input("enter cost price:-"))
selling_price=float(input("enter selling price:-"))
if cost_price<=0:
    print("enter an valid cost price")
else:
    if cost_price<selling_price:
        Profit =selling_price-cost_price
        print(Profit/cost_price*100)
    elif cost_price>selling_price:
        Loss = cost_price - selling_price 
        print("loss percentage=",(Loss/cost_price*100))

#16. Electricity Bill
print("Output for Question 16.................................................")
unit=int(input("enter your units:-"))
if unit>200:
    print((unit-200)*10+200*7+100*5)
elif unit>100 and unit<=200:
    print((unit-100)*7+100*5)
else:
    print(unit*5)


#17. Simple Calculator
print("Output for Question 17.................................................")
choice=int(input("enter your choice:-\n 1=addition \n 2=subtraction \n 3=multiplication \n 4=division \n"))
if choice>4:
    print("please enter valid choise!!!!")
else:
    num1=float(input("Enter your first number:-"))
    num2=float(input("Enter your second number:-"))
    if choice==1:
        print("addition",(num1+num2))
    elif choice==2:
        print("subtraction",(num1-num2))
    elif choice==3:
        print("multiplication",(num1*num2))
    elif choice==4:
        if num2!=0:
            print("divition",(num1/num2))
        else:
            print("num 2 is not equal to zero")
    elif choice>4 or choice<1:
        print("enter valid choise less than 4 or equal to")


#18. Temperature Classifier
print("Output for Question 18.................................................")
temp=float(input("enter temperature in calcius:-"))
if temp<0:
    print("Freezing")
elif temp>=0 and temp<=15:
    proint("Very Cold")
elif temp>=16 and temp<=25:
    print("Cold")
elif temp>=26 and temp<=35:
    print("Normal")
else:
    print("Hot")


#19. Number Range Checker
print("Output for Question 19.................................................")
num=int(input("enter an number:-"))
if num<0:
    print("negative")
elif num>=0 and num<=10:
    print(" number is Bitween 0 and 10")
elif num>=11 and num<=50:
    print(" number is Bitween 11 and 50")
elif num>=51 and num<=100:
    print(" number is Bitween 51 and 100")
else:
    print("greatre than 100")



#20. Triangle Validator
print("Output for Question 20.................................................")
x=float(input("enter first side of trinagle:-"))
y=float(input("enter second side of triange:-"))
z=float(input("Enter third side of triangle:-"))
if x+y>z and x+z>y and y+z>x:
    print("Valid triangel ")
else:
    print("invalid triangle")


#21. Triangle Type
print("Output for Question 21.................................................")
x=float(input("enter first side of trinagle:-"))
y=float(input("enter second side of triange:-"))
z=float(input("Enter third side of triangle:-"))
if x+y>z and x+z>y and y+z>x:
    if x==y==z:
        print("equilateral triangle")
    elif x==y or y==z or x==z:
        print("Isoscale triangle")
    else:
        print("Scalen triangle")
else:
    print("invalid triangle")


#22. ATM Withdrawal
print("Output for Question 22.................................................")
account_balance=float(input("enter your acount balance:-"))
with_balance=int(input("enter your withdrowl amount:-"))
account_balance=account_balance-with_balance
if with_balance>0 and with_balance%100==0 and with_balance<account_balance and account_balance>=500:
    print(f"withdeawl succesful \n remaining balance {account_balance}")
elif account_balance<500:
    print("minimum reched")
elif account_balance<0:
    print("no balance")
elif with_balance>account_balance:
    print("please check amount balance ")


#23. Login System
print("Output for Question 23.................................................")
username=input("enter username:-").strip()
password=input("enter your password:-").strip()
if username=="admin" or password=="python123":
    if username=="admin" and password=="python123":
        print("Login succesfully")
    elif username=="admin" or password!="python123":
        print("Wronge password")
    else:
        print("user not found")


#24. Discount Calculator
print("Output for Question 24.................................................")
amount=float(input("enter purchase amount:-"))
if amount<500:
    discount="0%"
    dis_amount=0
    final_amount=amount-dis_amount
    print(f"Purchase:{amount} \n discount:{discount} \n Discount amount: {dis_amount} \n Final amount:{final_amount}")
elif amount>=500 and amount<999:
    discount="5%"
    dis_amount=amount/5*100
    final_amount=amount-dis_amount
    print(f"Purchase:{amount} \n discount:{discount} \n Discount amount: {dis_amount} \n Final amount:{final_amount}")
elif amount>=1000 and amount<1999:
    discount="10%"
    dis_amount=amount/10*100
    final_amount=amount-dis_amount
    print(f"Purchase:{amount} \n discount:{discount} \n Discount amount: {dis_amount} \n Final amount:{final_amount}")
elif amount>=2000 and amount<4999:
    discount="15%"
    dis_amount=amount/15*100
    final_amount=amount-dis_amount
    print(f"Purchase:{amount} \n discount:{discount} \n Discount amount: {dis_amount} \n Final amount:{final_amount}")
elif amount>=5000:
    discount="20%"
    dis_amount=amount/20*100
    final_amount=amount-dis_amount
    print(f"Purchase:{amount} \n discount:{discount} \n Discount amount: {dis_amount} \n Final amount:{final_amount}")


#25. Student Result System
print("Output for Question 25.................................................")
marks1=int(input("Enter your sub 1 marks:-"))
marks2=int(input("enter your sub2 marks:-"))
marks3=int(input("enter your sub3 marks:-"))
if (marks1<0 or marks1>100) or (marks2<0 or marks2>100) or (marks3<0 or marks3>100):
    print("enter valid marks")
elif marks1<35 or marks2<35 or marks3<35:
    print("fail")
else:
    avg=(marks1+marks2+marks3)/3
    if avg>=75:
        print("Distinction")
    elif avg>=60 and avg<=74:
        print("First class")
    elif avg>=50 and avg<=59:
        print("First class")
    else:
        print(Pass)


#26. Date Validator
print("Output for Question 26.................................................")
day=int(input("enter day :-"))
month=int(input("enter month:-"))
year=int(input("enter year:-"))
if 0<day<32 and 0<month<13 and year>0:
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (year%400!=0 or year%4!=0 and year%100!=0):
        print("valid year")
    elif (month==4 or month==6 or month==9 or month==11) and (year%400!=0 or year%4!=0 and year%100!=0) and 0<day<31:
        print("valid year")
    else:
        if (year%400==0 or year%4==0 and year%100==0) and 0<day<30:
            print("Leap year ")
        elif (year%400!=0 or year%4!=0 and year%100!=0) and 0<day<29:
            print("valid year")
        else:
            print("enter valid day")
else:
    print("Enter an valid data")

#27. Time Validator
print("Output for Question 27.................................................")
seconds=int(input("enter seconds:-"))
minutes=int(input("enter minuts:-"))
hours=int(input("enter hours:-"))
if (0<seconds<60) and (0<minutes<60) and (0<hours<13):
    print("valid time ")
else:
    print(" please enter an valid time")


#28. Youngest of Three People
print("Output for Question 28:.................................................")
name_person1=input("Enter your name:")
age_person1=int(input("Enter your age:"))
name_person2=input("Enter your name:")
age_person2=int(input("Enter your age:"))
name_person3=input("Enter your name:")
age_person3=int(input("Enter your age:"))
if age_person1<age_person2 and age_person1<age_person3:
    print(f"{name_person1} is the youngest")
elif age_person2<age_person1 and age_person2<age_person3:
    print(f"{name_person2} is the youngest")
elif age_person3<age_person2 and age_person3<age_person1:
    print(f"{name_person3} is the youngest")  
elif age_person1==age_person2==age_person3:
    print("all are same age")
else:
    if age_person1==age_person2!=age_person3:
        print(f"{name_person1} and {name_person2} are same age")
    elif age_person3==age_person2!=age_person1:
        print(f"{name_person3} and {name_person2} are same age")
    else:
        print(f"{name_person1} and {name_person3} are same age")      


#29. Second Largest of Three Numbers
print("Output for Question 29:.................................................")
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"Middle number is {num2}")
    else:
        print(f"Middle number is {num3}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"Middle number is {num1}")  
    else:
        print(f"Middle number is {num3}") 
elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"Middle number is {num1}")
    else:
        print(f"Middle number is {num2}")                     
elif num1==num2==num3:
    print(f"Middle number is {num2}")
else:
    if num1==num2:
        print(f"Middle number is {num2}")
    elif num1==num3:
        print(f"Middle number is {num1}")
    else:
        print(f"Middle number is {num2}") 


#30. Complete Scholarship Decision
print("Output for Question 30:.................................................")
student_age=int(input("Enter student age:"))
marks=int(input("Enter student marks:"))
family_income=int(input("Enter family income:"))
attendance_percentage=int(input("Enter student attendance percentage:"))
if 18<=student_age<=25 and 85<=marks<=100 and 0<=family_income<=30000 and  75<=attendance_percentage<=100:
    print("Scholarship Approved")
elif not 18<=student_age<=25:
    print("Scholarship Rejected \nReason: Student age is not satisfied")
elif not 85<=marks<=100:
    print("Scholarship Rejected \nReason: Marks below 85")
elif not 0<=family_income<=30000:
    print("Scholarship Rejected \nReason: family income more than 30000") 
elif not 75<=attendance_percentage<=100:
    print("Scholarship Rejected \nReason: attendance is less than 75%")      
else:
    print("Enter valid values")