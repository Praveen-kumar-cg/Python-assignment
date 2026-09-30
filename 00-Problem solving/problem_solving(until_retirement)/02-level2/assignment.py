#Q11
for i in range(11):
    print(i,end=" ")

#Q12
num=int(input("enter an number:-"))
for i in range(num+1):
    print(i,end=" ")

#Q13
num=int(input("enter an number:-"))
for i in range(2,num+1,2):
    print(i,end=" ")

#Q14
num=int(input("enter an number:-"))
for i in range(1,num+1,2):
    print(i,end=" ")

#Q15
num=int(input("enter an number:-"))
total=0
for i in range(num+1):
    total+=i
print("the total is ",total)

#Q16
num=int(input("enter an number:-"))
product=1
for i in range(1,num+1):
    product*=i
print("the product is ",product)

#Q17
num=int(input("enter an number"))
i=1
while i<=num:
    j=1
    while j<=10:
        print(i*j,end=" ")
        j+=1
    print()
    i+=1


#Q18
num=int(input("enter an number:-"))
count=0
for i in range(1,num+1):
    if i%3==0:
        count+=1
    
print("the count is ",count)


#Q19
num=int(input("enter an number:-"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("the factorial is ",factorial)


#Q20
num=int(input("enter an number:-"))
count=0
for i in range(num+1):
    if i%7==0:
        count+=1
print("the count is ",count)
