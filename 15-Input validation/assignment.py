#Part A — Intermediate Problems

#Problem 1: Valid Marks

while True:
    marks=int(input("enter your marks:-"))
    if 0<=marks<=100:
        print("valid marks")
        print(marks)
        break
    else:
        marks=int(input("enter your valid marks:-"))


#Problem 2: Positive Integer
while True:
    num=int(input("enter the numbers:-"))
    if num>0:
        print("number is accepted")
        break
    else:
        num=int(input("enter the numbers:-"))


#Problem 3: Age Validation
while True:
    age=int(input("enter your age:-"))
    if 0<=age<=120:
        print("valid age")
        break
    else:
        age=int(input("enter your age:-"))


#Problem 4: Menu Choice
choice=int(input("enter your choice:\n1>=View Profile\n2=>Edit Profile\n3=>Settings\n4=>Exit\n>>>>>>>>"))
match choice:
    case 1:
        print("selected view profile")
    case 2:
        print("selected edit profile")
    case 3:
        print("selected settings")
    case 4:
        print("selected exit")
    case _:
        choice=int(input("enter your correct choice:\n1>=View Profile\n2=>Edit Profile\n3=>Settings\n4=>Exit\n>>>>>>>>"))


#Problem 5: Password Length
while True:
    Pass=input("enter your passsword:-").strip()
    passlength=len(str(Pass))
    if passlength>=8:
        print("valid passsword")
        break
    else:
        Pass=input("enter your passsword:-").strip()


#Problem 6: Temperature Range
while True:
    temp=int(input("enter your temp:-"))
    if -20<=temp<=45:
        print("valid temperature")
        break
    else:
        temp=int(input("enter your temp:-"))


#Problem 7: Withdrawal Validation
bank_balance=5000
while True:
    amount=int(input("enter an amount ot withderawl:-"))
    if amount<=bank_balance and amount>0:
        print("succesfully withdrawl")
        bank_balance-=amount
        break
    else:
        amount=int(input("enter an valid amount"))

print(bank_balance)


#Problem 8: Username Validation
while True:
    name=input("enter your username:-").strip()
    if (len(name)>5) and name!="" and " " not in name:
        print("valid name")
        print(name)
        break
    else:
        print("Invalid marks. Try again.")


#Problem 9: Divisible Number
while True:
    num9=int(input("enter an number:-"))
    if num9>0 and num9%3==0 and num9%5==0:
        print(num9,"valid number")
        break
    else:
        print("enter an valid number")


#Problem 10: Limited PIN Attempts
PIN=2465
for i in range(1,4):
    user_pin=int(input("enter your pin;-"))
    if user_pin==PIN:
        print("login succesffuly")
        break
    else:
        print("enter an valid pin")
else:
    print("All ataimped fail come tommorow")


#Problem 11: Number Within a Range
while True:
    num11=int(input("enter an number bitween 10 to50:-"))
    if 10<=num11<=50:
        if num11%2==0:
            print("even")
        else:
            print("odd")
        break
    else:
        print("enter an valid number;")


#Problem 12: Deposit Validation
balance=2000
while True:
    deposite=int(input("enter the amount that want to deposite:-"))
    if deposite>0:
        balance+=deposite
        print(balance)
        break
    else:
        print("enter an valid amount ")


#Problem 13: Integer Between 1 and 100
while True:
    num13=int(input("enter an number:-"))
    if 1<=num13<=100:
        print("valid")
        break
    else:
        print("emter an valid number")


#Problem 14: Marks and Result

while True:
    marks14=int(input("enter your marks:-"))
    if marks14<0 or marks14>100:
        print("enter an valid number")
    else:
        if marks14>=75:
            print("distinction")
            break
        elif 60<=marks14<75:
            print("fist class")
            break
        elif 35<=marks14<60:
            print("pass")
            break
        else:
            print("fail")
            break


#Problem 15: Username and Password Validation
while True:
    username = input("Enter the username:- ").strip()
    password = input("Enter the password:- ")

    if len(username) >= 5 and " " not in username and len(password) >= 8 and password.strip() != "":
        print("Login details are valid!")
        break
    else:
        print("Invalid username or password. Please try again.")


#Problem 16: Calculator Input Validation
while True:
    choice16=int(input("enter your choice\n 1=+\n2=-\n3=*\n4=/\n>>>>>"))
    if choice16>4 or choice16<1:
        print("enter an valid choice")
    else:
        num1=int(input("enter the first number:-"))
        num2=int(input("enter second number:-"))
        if choice16==1:
            sum=num1+num2
            print(sum,"addition")
            
        elif choice16==2:
            sub=num1-num2
            print(sub,"subtraction")
        elif choice16==3:
            mul=num1*num2
            print(mul,"multiplication")
        else:
            while num2==0:
                print("invalid input")
                num2=int(input("enter the second number again:-"))
            else:
                div=num1/num2
                print(div,"division")

        break


#17
balance = 10000
while True:
    choice=int(input("enter your choice\n1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit\n>>>>>>"))
    if choice == 1:
        print(balance)
    elif choice == 2:
        deposit_amount = int(input("Enter the amount to deposit: "))
        while deposit_amount<0:
            print("enter an valid amount")
        else:
            balance += deposit_amount
    elif option == 3:
        withdrawl_amount = int(input("Enter the amount to withdrawl: "))
        while withdrawl_amount < 0 or withdrawl_amount > balance:\
            print("enter an valid input")
        else:
            balance -= withdrawl_amount
    else:
        print("Banking Menu Exited")

#18
while True:
    month=int(input("enter the month:-"))
while month < 1 or month > 12 or day > 31 or day < 1:
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
else:
    print("Day and Month Accepted")
            
            

