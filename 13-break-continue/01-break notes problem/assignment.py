#Problem 1
for i in range(1,11):
    if i==6:
        break
    print(i)

# Problem 2
numbers = [10, 20, 30, 40, 50]
for ch in numbers:
    if ch==30:
        print("found")
        break


# Problem 3
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break

    print("You entered:", num)

# Problem 4
count=0
flag=False
for ch in range(101):
    if ch%17==0 and count<1:
        count+=1
        print("found")
        flag=True
if not flag:
    print("not found")
print(count)