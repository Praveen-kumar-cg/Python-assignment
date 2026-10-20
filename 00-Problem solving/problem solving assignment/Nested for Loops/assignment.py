# Level 1 — Nested Loop Basics
#Q1
for i in range(1,4):
    for j in range(1,4):
        print(i,j)


#Q2
num=int(input("enteer na numbe:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        print(f"{i} X {j} = {i*j}")


#Q3
row=int(input("enter the no. of rows:-"))
column=int(input("enter the no. of column:-"))
for i in range(row):
    for j in range(column):
        print("*",end="")
    print()
    

#Q4
row=int(input("enter the no. of rows:-"))
column=int(input("enter the no. of column:-"))
for i in range(row):
    for j in range(column):
        print(({i,j}),end=" ")
    print()
    

#Q5
row=int(input("enter the no. of rows:-"))
column=int(input("enter the no. of column:-"))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(i,end=" ")
    print()
    

#Q6
row=int(input("enter the no. of rows:-"))
column=int(input("enter the no. of column:-"))
for i in range(1,row+1):
    for j in range(1,column+1):
        print(j,end=" ")
    print()
    

#Q7
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


#Q8
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,row-i+2):
        print(j,end="")
    print()


Q9
row=int(input("enter the no. of rows:-"))
column=int(input("enter the no. of column:-"))
for i in range(row):
    for j in range(column):
        print("*",end="")
    print()
    

#Q10
row=int(input("enter the no. of rows:-"))
for i in range(row):
    for j in range(row):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()
    


#Level 2 — Conditions Inside Nested Loops
#Q11
row=int(input("enter the no. of rows:-"))
column=int(input("enter the no. of column:-"))
for i in range(1,row+1):
    for j in range(1,column+1):
        if j%2==0:
            print(j,end=" ")
    print()


#Q12
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if j%2!=0:
            print(j,end=" ")
    print()
    

#Q13
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if (i+j)%2==0:
            print("E",end=" ")
        else:
            print("O",end=" ")
    print()
    

#Q14
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==j:
            print("Same",end=" ")
        else:
            print("Different",end=" ")
    print()
    

#Q15
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()


#Q16
row=int(input("enter the no. of rows:-"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if i%j==0:
            print("X",end=" ")
        else:
            print("-",end=" ")
    print()


#Q17
N=int(input("enter the no.:-"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if j%i==0:
            print(j,end=" ")
    print()


#Q18
N=int(input("enter the no.:-"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if (i+j)>N:
            print(f"{i,j}")


#Q19
N=int(input("enter the no.:-"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if (i*j)%2==0:
            print(f"{i,j} {i*j}")


#Q20
N=int(input("enter the no.:-"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print("Special",end=" ")
        elif i+j==N:
            print("pair",end=" ")
        else:
            print("normal",end=" ")
    print()



# Level 3 — Strings + Nested Loops
#Q21
str=input("enter an string:-")
for ch in str:
    for i in range(3):
        print(ch,end="")
    print()


# Q22
str=input("enter an string:-")
for ch in str:
    for i in range(3):
        print(ch,i)

# Q23
text = input("Enter a string: ")
for i in text:
    for j in text:
        if i == j:
            print(i, j, "Same")
        else:
            print(i, j, "Different")


# Q24
str1=input("enter first string:-")
str2=input("enter second string:-")
for i in str1:
    for j in str2:
        if i==j:
            print(i,j)


# Q25
str1=input("enter first string:-")
str2=input("enter second string:-")
count=0
for i in str1:
    for j in str2:
        if i==j:
            count+=1
print(count)


# Q26
str1=input("enter first string:-")
for i in str1:
    count=0
    for j in str1:
        if i==j:
            count+=1
    print(i,count)


# Q27
str=input("enter an string:-")
for i in str:
    if i in "AEIOUaeiou":
        print(i,"=voval")
    else:
        print(i,"=consonent")


# Q28
str1=input("enter first string:-")
str2=input("enter second string:-")
for i in str1:
    for j in str2:
        if i==j:
            print(f"common character includes {j}")


# Q29
str1=input("enter first string:-")
for i in str1:
    for j in str1:
        print(i,j)



# Q30
str1=input("enter first string:-")
for i in str1:
    for j in str1:
        if i!=j:
            print(i,j)