# #Part A — Intermediate Problems

# #Problem 1: Valid Marks

# while True:
#     marks=int(input("enter your marks:-"))
#     if 0<=marks<=100:
#         print("valid marks")
#         print(marks)
#         break
#     else:
#         marks=int(input("enter your valid marks:-"))


# #Problem 2: Positive Integer
# while True:
#     num=int(input("enter the numbers:-"))
#     if num>0:
#         print("number is accepted")
#         break
#     else:
#         num=int(input("enter the numbers:-"))


# #Problem 3: Age Validation
# while True:
#     age=int(input("enter your age:-"))
#     if 0<=age<=120:
#         print("valid age")
#         break
#     else:
#         age=int(input("enter your age:-"))


# #Problem 4: Menu Choice
# choice=int(input("enter your choice:\n1>=View Profile\n2=>Edit Profile\n3=>Settings\n4=>Exit\n>>>>>>>>"))
# match choice:
#     case 1:
#         print("selected view profile")
#     case 2:
#         print("selected edit profile")
#     case 3:
#         print("selected settings")
#     case 4:
#         print("selected exit")
#     case _:
#         choice=int(input("enter your correct choice:\n1>=View Profile\n2=>Edit Profile\n3=>Settings\n4=>Exit\n>>>>>>>>"))


# #Problem 5: Password Length
# while True:
#     Pass=input("enter your passsword:-").strip()
#     passlength=len(str(Pass))
#     if passlength>=8:
#         print("valid passsword")
#         break
#     else:
#         Pass=input("enter your passsword:-").strip()


# #Problem 6: Temperature Range
# while True:
#     temp=int(input("enter your temp:-"))
#     if -20<=temp<=45:
#         print("valid temperature")
#         break
#     else:
#         temp=int(input("enter your temp:-"))


# #Problem 7: Withdrawal Validation
# bank_balance=5000
# while True:
#     amount=int(input("enter an amount ot withderawl:-"))
#     if amount<=bank_balance and amount>0:
#         print("succesfully withdrawl")
#         bank_balance-=amount
#         break
#     else:
#         amount=int(input("enter an valid amount"))

# print(bank_balance)


#Problem 8: Username Validation
# while True:
#     name=input("enter your username:-").strip()
#     if (len(name)>5) and name!="" and " " not in name:
#         print("valid name")
#         print(name)
#         break
#     else:
#         print("Invalid marks. Try again.")

