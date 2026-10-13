#A1. Output Prediction --- Easy


#Q1. Stop Before Printing 5
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")

#Output
#1
#2
#3
#4
#Finished

#Q2. Stop at the First Vowel
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)

#output
#s
#k
#y
#l


#Q3. break in a while Loop
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

#output
#2
#4
#6


#A2. Write a Program --- Medium

#Q4
limit=int(input("enter an limit:--"))
for i in range(1,limit+1):
    if i==7:
        break
    print(i)

#Q5
str5=input("enter an string:-").lower()
for ch in str5:
    print(ch,end="")
    if "p" in ch:
        break
        

#Q6
list6=[1,32,-78,345,2,24,0,-5,-58]
for ch in list6:
    if ch<0:
        break
    print(ch)


#A3. Think Carefully --- Challenging

#Q7
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

#output
#1 1
#1 2
#2 1
#2 2
#3 1
#3 2


#Q8
str8=input("enter an strig:-").lower().split()
for ch in str8:
    if "python" in ch:
        print("found")
        break
    else:
        print("not found")




#Section B --- Practice Problems on continue
#B1. Output Prediction --- Easy

#Q9
for i in range(1, 7):
    if i == 4:
        continue
    print(i)

#output
#1
#2
#3
#5
#6


#Q10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

#output
#dctn


#Q11
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

#output
#1
#2
#4
#5


#B2. Write a Program --- Medium
#Q12
num12=int(input("enter an number:-"))
for i in range(1,num12+1):
    if i%3==0:
        continue
    print(i)

#Q13
str13=input("enter an string:-")

for ch in str13:
    if ch=="s":
        continue
    print(ch,end="")

#Q14
marks = input("Enter marks: ").split()
for mark in marks:
    mark = int(mark)
    if mark < 40:
        continue
    print(mark, end=" ")

#B3. Think Carefully --- Challenging
#Q15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

#output
#A 1
# B 1
#A 3
# B 3
#A 4
#B 4


#Q16
n = 0
while n < 5:
    if n == 3:
        n+=1
        continue
    n += 1
    print(n)

#output
#1
#2
#3
#5

#Q17
str17=input("Enter an string:-").lower()
consonent_count17=0
for ch in str17:
    if ch in "aeiou":
        continue
    else:
        consonent_count17+=1

print(consonent_count17)

#Section C --- Practice Problems on for-else
#C1. Output Prediction --- Easy

#Q18
for i in range(1, 4):
    print(i)
else:
    print("Done")

#output
#1
#2
#3
#Done

#Q19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

#output
#1
#3
#4
#Completed


#Q20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

#output
#1
#2
#Outside loop

#Q21
for item in []:
    print("Inside")
else:
    print("Else block")

#output
#Else block

#C2. Write a Program --- Medium
#Q22
list22=[4, 8 ,12, 16]
for ch in list22:
    if ch==12:
        print("found")
        break
else:
    print("not found")

#Q23
str23=input("enter an string:-")
for ch in str23:
    if "g" in ch:
        print("character exit")
        break
else:
    print("character missing")

#Q24
num24=int(input("enter an nunber:-"))
for i in range(2,num24-1):
    if num24%i==0:
        print("not an prime number:-")
        break
        
else:
    print("prime number")


#C3. Think Carefully --- Challenging

#Q25
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")

#output
#All are even


#Q26
#Case A

for x in range(3):
    continue
else:
    print("A")

#output
#A

#Case B
for x in range(3):
    break
else:
    print("B")

#Case C
for x in range(0):
    print(x)
else:
    print("C")
##output
#C


#Q27
str27=input("enter an string:-")
for ch in str27:
    count=0
    for c in str27:
        if ch==c:
            count+=1
    if count>=2:
        print("repeted charcter")
        print(ch)
        break
else:
    print("no repeted character")


#Section D --- Practice Problems on pass
#D1. Output Prediction --- Easy

#Q28
for i in range(1, 4):
    if i == 2:
        pass
    print(i)

#output
#1
#2
#3


#Q29
x = 10

if x > 5:
    pass

print("Finished")

#output
#Finished


#Q30
for letter in "cat":
    pass

print("Loop ended")

#output
#Loop ended


#D2. Write a Program --- Medium

#Q31
for i in range(1,6):
    if i%2==0:
        pass
    print(i)

#Q32
choice32=int(input("enter your choice:-"))
if choice32==1:
    print("burgur selected")
elif choice32==2:
    pass
else:
    print("invalid choce")
print("program closed")


#D3. Think Carefully --- Challenging

#Q33
#Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

#output
#1
#2
#3
#4

#Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)

#output
#1
#2
#4

#Q34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


#Section E --- Mixed Challenge Questions

#Q35
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")

#output
#1
#3

#Q36
list36=[-2, 4 ,7 ,9]
for ch in list36:
    if ch<0:
        continue
    if ch==7:
        print("target found")
        break
else:
    print("target not found")

#Q37
list37=[2, 0, 4, -1, 8]
for ch in list37:
    if ch==0:
        continue
    if ch<0:
        print(ch)
        break
else:
    print("All value processed")


#Q38
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

#output
#1 1
#1 3
#Inner loop completed
#2 1
#2 3
#Inner loop completed

#Q39
list39=[-3, 8, 12, 24]
for ch in list39:
    if ch<0:
        continue
    if ch%4==0 and ch%6==0:
        print("found")
        break

else:
    print("no matching number")

#Q40
# 1. Stop searching after finding a username
for name in ["Amit", "Raj", "Priya"]:
    if name == "Raj":
        print("Username found")
        break

# 2. Skip blank strings
strings = ["Hello", "", "Python"]
for s in strings:
    if s == "":
        continue
    print(s)

# 3. Display "Not found" if no match exists
for name in ["Amit", "Raj", "Priya"]:
    if name == "Rahul":
        print("Found")
        break
else:
    print("Not found")

# 4. Keep an unfinished function valid
def my_function():
    pass

# 5. Skip the current number
for n in [10, 20, 30, 40]:
    if n == 20:
        continue
    print(n)

# 6. Stop when the user enters 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    print(n)

# 7. Report that all items were checked if no match caused an early stop
for item in ["Pen", "Book", "Pencil"]:
    if item == "Phone":
        print("Match found")
        break
else:
    print("All items were checked")

# 8. Leave a conditional block empty
number = 10
if number > 0:
    pass