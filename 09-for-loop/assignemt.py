#A. Basic for Loop
#1
print("Output for question-1..............................................................")
for i in range(5):
    print("Hello")

#2
print("Output for question-2..............................................................")
for i in range(10):
    print(i,end=" ")

#3
print("\nOutput for question-3..............................................................")
for i in range(1,11):
    print(i)

#4
print("Output for question-4..............................................................")
for i in range(10,0,-1):
    print(i)

#5
print("Output for question-5..............................................................")
for i in range(5,51,5):
    print(i)

#6
print("Output for question-6..............................................................")
for i in range(2,21):
    if i%2==0:
        print(i,"even number")

#7
print("Output for question-7..............................................................")
for i in range(1,20):
    if i%2!=0:
        print(i,"odd number")

#8
print("Output for question-8..............................................................")
for i in range(3,20,3):
    print(i,end=" ")


#9
print("\nOutput for question-9..............................................................")
for i in range(20,1,-2):
    print(i)


#10
print("Output for question-10..............................................................")
num=int(input("enter an positive number:-"))
if num<=0:
    print("enter an positive number")
else:
    for i in range(1,num+1):
        print(i)

#11
print("Output for question-11..............................................................")
num=int(input("enter an positive number:-"))
if num<0:
    print("enter an positive number")
else:
    for i in range(2,num+1,2):
        print(i)


#12
print("Output for question-12..............................................................")
num=int(input("enter an positive number:-"))
if num<0:
    print("enter an positive number")
else:
    for i in range(1,num+1,2):
        print(i)


#13
print("Output for question-13..............................................................")
num=int(input("enter an positive number:-"))
if num<0:
    print("enter an positive number")
else:
    for i in range(0,num+1,3):
        print(f"{i} divisible by 3")
        


#14
print("Output for question-14..............................................................")
num=int(input("enter an positive number:-"))
if num<0:
    print("enter an positive number")
else:
    for i in range(1,num+1,):
        if i%2==0 and i%3==0:
            print(f"{i} divisible by both 2 and 3")
        

#15
print("Output for question-15..............................................................")
num=int(input("enter an positive number:-"))
count=0
for i in range(1,num+1):
    if i%2==0:
        count=count+1
print("total enen number is",count)


#16
print("Output for question-16..............................................................")
num=int(input("enter an positive number:-"))
sum=0
for i in range(0,num+1):
    sum=sum+i
print("sum is ",sum)


#17
print("Output for question-17..............................................................")
num=int(input("enter an positive number:-"))
sum=0
if num<0:
    print("enter an positive number")
else:
    for i in range(0,num+1,2):
        sum=sum+i
print("The sum of even is ",sum)


#18
print("Output for question-18..............................................................")
num=int(input("enter an positive number:-"))
sum=0
if num<0:
    print("enter an positive number")
else:
    for i in range(1,num+1,2):
        sum=sum+i
print("The sum of odd is ",sum)


#19
print("Output for question-19..............................................................")
num=int(input("enter an positive number:-"))
if num<0:
    print("enter an positive number")
else:
    for i in range(1,11,):
        print(f"{num}*{i}={num*i}")

#20
print("Output for question-20..............................................................")
num=int(input("enter an positive number:-"))
mul=1
for i in range(1,num+1):
    mul=mul*i
print("the multiplecation is",mul)

#21
print("Output for question-21..............................................................")
name_ch=input("enter your name:-")
for i in name_ch:
    print(i)

#22
print("Output for question-22..............................................................")
name_ch=input("enter your name:-")
for i in name_ch:
    print(i,end=" ")

#23
print("Output for question-23..............................................................")
name_ch=input("enter your name:-")
count=0
for i in name_ch:
    count=count+1
print(count)

#24
print("Output for question-24.............................................................")
name_ch=input("enter your name:-")
count=0
for i in name_ch:
    if i=="a":
        count=count+1
print(count)

#25
print("Output for question-25.............................................................")
name_ch=input("enter your name:-")
count=0
for i in name_ch:
    if ord(i)<=91 and ord(i)>=65:
        count=count+1
print("the upper case leter is",count)



