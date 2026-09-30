# #1. digit_count and Character Analyzer
# upper_count=0
# space_count=0
# digit_count=0
# space_count=0
# special_char=0
# str1=input("Enter an string:-")
# print("The string is :-",str1)
# for ch in str1:
#     if chr(65)<=ch<=chr(90):
#         upper_count+=1
#     elif chr(97)<=ch<=chr(122):
#         space_count+=1
#     elif chr(32)==ch:
#         space_count+=1
#     elif chr(48)<=ch<=chr(57):
#         digit_count+=1
#     else:
#         special_char+=1
# if upper_count > space_count and upper_count > digit_count and upper_count > space_count and upper_count > special_char:
#     print("Highest: upper_countcase")

# elif space_count > upper_count and space_count > digit_count and space_count > space_count and space_count > special_char:
#     print("Highest: space_countcase")

# elif digit_count > upper_count and digit_count > space_count and digit_count > space_count and digit_count > special_char:
#     print("Highest: digit_counts")

# elif space_count > upper_count and space_count > space_count and space_count > digit_count and space_count > special_char:
#     print("Highest: space_counts")

# elif special_char > upper_count and special_char > space_count and special_char > digit_count and special_char > space_count:
#     print("Highest: Special characters")

# else:
#     print("Tie")
# print("upper_countcase:-",upper_count)
# print("space_countcase:-",space_count)
# print("digit_count:-",digit_count)
# print("space_count:-",space_count)
# print("special:-",special_char)


# #2. Student Performance Analyzer
# fail_count=0
# pass_count=0
# good_count=0
# excellent_count=0
# for i in range(1,11):
#     marks=int(input("enter your marks:-"))
#     if marks<0 or marks>100:
#         print("enter valid marks")
#     else:

#         if marks<35:
#             print("fail")
#             fail_count+=1
#         elif 35<=marks<=49:
#             print("pass")
#             pass_count+=1
#         elif 50<=marks<=74:
#             print("good")
#             good_count+=1
#         else:
#             print("excellent")
#             excellent_count+=1
# print("The number of student fail:-",fail_count)
# print("The number of student pass:-",pass_count)
# print("The number of student score good:-",good_count)
# print("The number of student score excellent:-",excellent_count)


# #3. Word Score Calculator
# voval_point=0
# consonent_point=0
# digit_point=0
# special_ch_point=0
# str2=input("enter an santance:-")
# for ch in str2:
#     if ch in "AEIOUaeiou":
#         voval_point+=2
#     elif "A" <= ch <= "Z" or "a" <= ch <= "z":
#         consonent_point += 1
#     elif chr(48)<=ch<=chr(57):
#         digit_point+=3
#     else:
#         special_ch_point+=4
# print("The point of voval is:-",voval_point)
# print("The point of consonent is:-",consonent_point)
# print("The point of digit is:-",digit_point)
# print("The point of special charater  is:-",special_ch_point)

# #4. Password Batch Validator
# for i in range(1,6):
#     Pass=input("enter your password:-")
#     is_minlength=False
#     is_uppercase=False
#     is_lowercase=False
#     is_digit=False
#     is_special=False
#     if len(Pass)>=8:
#         is_minlength=True
#     for j in Pass:
#         if chr(57)<=j<=chr(90):
#             is_uppercase=True
#         elif chr(97)<=j<=chr(122):
#             is_lowercase=True
#         elif chr(48)<=j<=chr(57):
#             is_digit=True
#         else:
#             is_special=True
#     count=(int(is_minlength)+int(is_uppercase)+int(is_lowercase)+int(is_digit)+int(is_special))
#     if count==5:
#         print("Strong Pass")
#     elif 3<=count<=4:
#         print("Medium password")
#     else:
#         print("weak password")



# #5. Sentence Word Analyzer
# short_count=0
# medium_count=0
# large_count=0
# sentance1=input("Enter an santance:-")
# list=sentance1.split()
# for i in list:
#     length=len(i)
#     if length<=3:
#         print(i,"Short")
#         short_count+=1
#     elif 4<=length<=6:
#         print(i,"Medium")
#         medium_count+=1
#     else:
#         print(i,"large")
#         large_count+=1
# print("number of short word:-",short_count)
# print("number of medium word:-",medium_count)
# print("number of long word:-",large_count)


# #6. Number-String Conversion Challenge
# even_count=0
# odd_count=0
# for i in range(5):
#     num=int(input("enter an number:-"))
#     num=str(num)
#     for j in num:
#         if int(j)%2==0:
#             even_count+=1
#         else:
#             odd_count+=1
# if even_count>odd_count:
#     print("even count is more in numbers",even_count)
# elif even_count<odd_count:
#     print("odd count is more in numbers:",odd_count)
# else:
#     print("Equal")



# #7. Repeated Character Report
# str1 = input("Enter a string: ")
# for char in str1:
#     count_char = 0

#     for char1 in str1:
#         if char == char1:
#             count_char+= 1

#     if count_char > 1:
#         if count_char == 2:
#             print(char, "->", count_char, "Duplicate")
#         elif count_char <= 4:
#             print(char, "->", count_char, "Repeated")
#         else:
#             print(char, "->", count_char, "Highly Repeated")



# #8. Shopping Cart Analyzer
# budget_count=0
# regular_count=0
# primum_count=0
# luxury_count=0
# total_price=0
# for i in range(8):
#     product_price=float(input("enter product price:-"))
#     total_price+=product_price
#     if product_price<500:
#         print("budget")
#         budget_count+=1
#     elif 500<=product_price<=1999:
#         print("regular")
#         regular_count+=1
#     elif 2000<=product_price<=4999:
#         print("Primum")
#         primum_count+=1
#     else:
#         print("luxuary")
#         luxury_count+=1
# average=total_price/8
# print("The total price of all product is :-",total_price)
# print("the product in budget catagory is ",budget_count)
# print("the product in regular catagory is ",regular_count)
# print("the product in primum catagory is ",primum_count)
# print("the product in luxury catagory is ",luxury_count)
# print("the average of all is ",average)



# #9. Character Position Challenge
# voval_count=0
# consonent_count=0
# digit_count=0
# special_count=0
# str3=input("enter an string:-")
# for ch in str3:
#     print(ch,"->",end="")
#     position=str3.find(ch)
#     print(position,"-",end="")
#     if position%2==0:
#         print("even")
#     else:
#         print("odd")
#     if ch in "AEIOUaeiou":
#         voval_count+=1
#     elif "A" <= ch <= "Z" or "a" <= ch <= "z":
#         consonent_count+= 1
#     elif chr(48)<=ch<=chr(57):
#         digit_count+=1
#     else:
#         special_count+=1

# print("the voval in the santance is :",voval_count)
# print("the consonent in the santance is :",consonent_count)
# print("the digit in the santance is :",digit_count)
# print("the special in the santance is :",special_count)



# #10. Number Pattern With Conditions
# n=int(input("Enter an number:-"))
# for i in range(n):
#     for j in range(1,i*2+2):
#         if j%3==0 and j%5==0:
#                 print("Z",end=" ")
#         elif j%3==0:
#                 print("X",end=" ")
#         elif j%5==0:
#                 print("Y",end=" ")
#         else:
#             print(j,end=" ")

#     print()



# #11. Username Analyzer
# for i in range(5):
#     is_length=False
#     is_first_char=False
#     digit_count=0
#     is_digit=False
#     is_underscore=False
#     count_underscore=0
#     is_invalid=False
#     user_name=input("enter username:-")
#     length=len(user_name)
#     if length>=8:
#         is_length=True
#     for ch in user_name:
#         first_char=ch[0]
#         if chr(97)<=first_char<=chr(122):
#             is_first_char=True
        
#         if chr(48)<=ch<=chr(57):
#             digit_count+=1
#         elif ch=="_":
#             count_underscore+=1
#             is_underscore=True
#         else:
#             is_invalid=True
#     if digit_count<2:
#         is_digit=False
#     else:
#         is_digit=True

#     score_count=(int(is_length)+int(is_first_char)+int(is_digit)+int( not is_invalid)+int(is_underscore))
#     if score_count==5:
#         print("Valid")
#     elif 3<=score_count<=4:
#         print("Need improvment")
#     else:
#         print("Invalid!!!")
#     print("length:",length)
#     print("digits:",digit_count)
#     print("underscore:",count_underscore)

    

# #12. Vowel-Consonant Battle
# voval_count=0
# a_count=e_count=i_count=o_count=u_count=0
# cons_count=0
# str6=input("enter an santance:-")
# for ch in str6:
#     if ch in "AEIOUaeiou":
#         voval_count+=1
#         if ch in "Aa":
#             a_count+=1
#         elif ch in "eE":
#             e_count+=1
#         elif ch in "Ii":
#             i_count+=1
#         elif ch in "Oo":
#             o_count+=1
#         else:
#             u_count+=1

#     elif "A"<=ch<="Z" or "a"<=ch<="z":
#         cons_count+=1

# if voval_count>cons_count:
#     print("Voval-win")
# elif voval_count<cons_count:
#     print("consonants -win")
# else:
#     print("Drow")

# print("A voval count is:-",a_count)
# print("E voval count is:-",e_count)
# print("I voval count is:-",i_count)
# print("O voval count is:-",o_count)
# print("u voval count is:-",u_count)



# #13. Electricity Bill Calculator
# for i in range(6):
#     units=int(input("Enter your units:-"))
#     total_bill=0
#     if units<=100:
#         total_bill=(units*5)
#     if units<=200:
#         total_bill=((units-100)*7)+500
#     if units<=400:
#         total_bill=((units-200)*10)+1200
#     else:
#         total_bill=((units-400)*15)+3200
    
#     if total_bill<1000:
#         print("Low")
#     elif 1000<=total_bill<=3000:
#         print("Medium")
#     else:
#         print("High")
#     print("The totka bill amount is -",total_bill)



# #14. Word Character Balance

# str7=input("enter an santance:-").split()
# length=len(str7)
# for word in str7:
#     voval_count=0
#     consonent_count=0
#     for ch in word:
#         if ch in "AEIOUaeiou":
#             voval_count+=1
#         elif "A"<=ch<="Z" or "a"<=ch<="z":
#             consonent_count+=1
#     if voval_count>consonent_count:
#         print("voval heavy")
#     elif voval_count<consonent_count:
#         print("consonent heavy")
#     else:
#         print("balanced")
#     print(f"For the word -{word}- the number of voval are {voval_count}")
#     print(f"For the word -{word}-the number of consonents are {consonent_count}")
        

# #15. Matrix Value Analyzer
# even_count=0
# odd_count=0
# positive_count=0
# negative_count=0
# zero_count=0
# largest=None
# for row in range(1,4):
#     for coloum in range(1,4):
#         num=int(input(f"Enter number for position {row}*{coloum} :-"))
#         if num%2==0:
#             print(num,">=is even",end=" ")
#             even_count+=1
#         else:
#             print(num,">=is odd",end=" ")
#             odd_count+=1
#         if num>0:
#             print("and positive")
#             positive_count+=1
#         elif num<0:
#             print("and negative")
#             negative_count+=1
#         else:
#             print("and zero")
#             zero_count+=1
#         if largest is None:
#             largest = num
#         elif num > largest:
#             largest = num
# print("The even count is ",even_count)
# print("The odd count is ",odd_count)
# print("The positive count is ",positive_count)
# print("The negative count is ",negative_count)
# print("The zero count is ",zero_count)
# print("The largest number is ",largest)



# #16. Password Character Distribution
# Password=input("enter an password:-")
# length=len(Password)
# voval_count=0
# consonent_count=0
# digit_count=0
# special_count=0
# for ch in Password:
#     if ch in "AEIOUaeiou":
#         voval_count+=1
#     elif "A"<=ch<="Z" or "a"<=ch<="z":
#         consonent_count+=1
#     elif chr(48)<=ch<=chr(57):
#         digit_count+=1
#     else:
#         special_count+=1


# voval_percantage=(voval_count*100)/length
# consonent_percantage=(consonent_count*100)/length
# digit_percantage=(digit_count*100)/length
# special_percantage=(special_count*100)/length
# if voval_percantage>consonent_percantage and voval_percantage>digit_percantage and voval_percantage>special_percantage:
#     print("voval category domenance")
# elif consonent_percantage>voval_percantage and consonent_percantage>digit_percantage and consonent_percantage>special_percantage:
#     print("consonent category dominanec")
# elif digit_percantage>voval_percantage and digit_percantage> consonent_percantage and digit_percantage>special_percantage:
#     print("digit catogery dominance")
# elif special_percantage>voval_percantage and special_percantage>consonent_percantage and special_percantage>digit_percantage:
#     print("specal count category")
# else:
#     print("tie")


# # 17. Student Name and Marks
# highest=0
# topper=""
# for i in range(5):
#     voval_count=0
#     consonent_count=0
#     student_name=input("Enter your name:-")
#     marks=int(input("Enter the marks:-"))
#     if marks<0 or marks>100:
#         print("please enter an valid marks:-")
#     else:
#         length=len(student_name)
#         for ch in student_name:
#             if ch in "AEIOUaeiou":
#                 voval_count+=1
#             elif "A"<=ch<="Z" or "a"<=ch<="z":
#                 consonent_count+=1
#         if marks>=90:
#             print("A")
#         elif 80<=marks<=89:
#             print("B")
#         elif 70<=marks<=79:
#             print("C")
#         elif 60<=marks<=69:
#             print("D")
#         elif 50<=marks<=59:
#             print("E")
#         else:
#             print("F")
#     if marks>highest:
#         highest=marks 
#         topper=student_name
# print("The highest marks of  class is ",topper,"and the marks are ",highest)        


# #18. ATM Transaction Analyzer
# initial_balance=20000
# transaction_count=0
# for i in range(7):
#     deposit=int(input("Enter the your deposit amount:-"))
#     withdrawal=int(input("Enter the withdrawal amount:-"))
#     if deposit:
#         initial_balance+=deposit
#         transaction_count+=1
#     if withdrawal:
#         if withdrawal>initial_balance:
#             print("Balance is insufficient!!")
#         elif initial_balance<1000:
#             print("low balance,no withdrowal")
#         else:
#             initial_balance-=withdrawal
#             transaction_count+=1
        
# print("the final amount in the account is ",initial_balance)
# print("the number of transaction count",transaction_count)


# # 19. Sentence Security Scanner
# is_digit=False
# url_like_txt=False
# at_the_rate=False
# special_char=False
# pass_patern=False
# para=input("enter an sentance :-")
# for ch in para:
#     if chr(48)<=ch<=chr(57):
#         is_digit=True
#     elif "A"<=ch<="Z" or "a"<=ch<="z":
#         pass_patern=True
#     elif ch==".":                                                                                               //dought in this question about pass like pattern
#         url_like_txt=True
#     elif ch=="@":
#         at_the_rate=True
#     else:
#         special_char=True

# count=(int(is_digit)+int(url_like_txt)+int(at_the_rate)+int(special_char)+int(pass_patern))
# if count==5:
#     print("Safe")
# elif 3<=count<=4:
#     print("Review")
# else:
#     print("Suspicious")



# #20. Multiplication Grid Analyzer
# n=int(input("enter an number for grid:-"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         grid=i*j
#         if grid%5==0:
#             print("F",end=" ")
#         elif grid%2==0:
#             print("E",end=" ")
#         else:
#             print("O",end=" ")
#     print()


# #21. Shopping Discount System
# total_bill=0
# final_price=0
# total_discount=0
# count_discount_20=0
# count_discount_15=0
# count_discount_10=0
# count_no_discount=0
# for i in range(10):
#     prodect_price=float(input("enter the product price:-"))
#     total_bill+=prodect_price
#     if prodect_price>=5000:
#         discount_price=(prodect_price*0.2)
#         final_price+=prodect_price-discount_price
#         total_discount+=discount_price
#         count_discount_20+=1
#     elif prodect_price>=3000:
#         discount_price=(prodect_price*0.15)
#         final_price+=prodect_price-discount_price
#         total_discount+=discount_price
#         count_discount_15+=1
#     elif prodect_price>=1000:
#         discount_price=(prodect_price*0.1)
#         final_price+=prodect_price-discount_price
#         total_discount+=discount_price
#         count_discount_10+=1
#     else:
#         discount_price=0
#         final_price+=prodect_price-discount_price
#         total_discount+=discount_price
#         count_no_discount+=1
# print("The total price of product is",total_bill)
# print("The final price of the all product is ",final_price)
# print("the total discount applyed to all product ",total_discount)
# print("20% discount count is ",count_discount_20)
# print("15% discount count is ",count_discount_15)
# print("10% discount count is ",count_discount_10)
# print("0% discount count is ",count_no_discount)



# #22. String Compression Counter
# str=input("enter an string with repeted later:-")
# for ch in str:
#     ch_count=0
#     for nch in str:                                                              # dought the character repete more than 1 time
#         if ch==nch:
#             ch_count+=1
#     print(f"ch,ch_count",end="")
# sentence = input("Enter sentence:")

#laya hua code
# a=0
# for i in sentence:
#     count = 0
#     for j in sentence:
#         if i==j:
#             count += 1
#     already_printed = False
#     for k in range(a):  
#         if i == sentence[k]:
#             already_printed = True 
#     a+=1                           
#     if count > 1 and not already_printed:
#         print(i+str(count),end="")


# #23. Employee Salary Analyzer
# total_salary=0
# junior_count=0
# mid_count=0
# senior_count=0
# executive_count=0
# for i in range(8):
#     salaries=int(input("enter your salary:-"))
#     total_salary+=salaries
#     if salaries<25000:
#         print("Junior")
#         junior_count+=1
#     elif 25000<=salaries<=50000:
#         print("Mid")
#         mid_count+=1
#     elif 50001<=salaries<=100000:
#         print("Senior")
#         senior_count+=1
#     else:
#         print("executive")
#         executive_count+=1
# average_salary=total_salary/8
# print("The junior count is",junior_count)
# print("The mid count is",mid_count)
# print("The senior count is",senior_count)
# print("The executive count is",executive_count)
# print("the average salary of all member is ",average_salary)


# #24. Secret Word Detector
# str=input("Enter an santance and decrate word:-").split()
# secrate_word="pointbreak"
# for ch in str:
#     for i in secrate_word:
#         present=ch
    



# #46. Number Box Pattern
# n=int(input("enter an number:-"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n:
#             print("*",end=" ")
#         else:
#             if j==1 or j==n:
#                 print("*",end=" ")
#             elif j%2==0:
#                 print("E",end=" ")
#             else:
#                 print("O",end=" ")
#     print()


#47. Inventory Analyzer
out_of_stock_count=0
critical_count=0
low_count=0
available_count=0
for i in range(8):
    quantity=int(input("enter the quantity of product:-"))
    if quantity==0:
        print("Out of stock")
        out_of_stock_count+=1
    elif 1<=quantity<=5:
        print("Critical")
        critical_count+=1
    elif 6<=quantity<=20:
        print("Low")
        low_count+=1
    else:
        print("Available")
        available_count+=1
if out_of_stock_count>critical_count and out_of_stock_count