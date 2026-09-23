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



#13. Electricity Bill Calculator
for i in range(6):
    units=int(input("Enter your units:-"))
    total_bill=0
    if units<=100:
        total_bill=(units*5)
    if units<=200:
        total_bill=((units-100)*7)+(100*5)
    if units<=400:
        total_bill=((units-200)*10)+1200
    else:
        total_bill=((units-400)*15)+3200
