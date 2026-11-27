# Q1

def show(n):
    if n == 0:
        print("Stop")
        return

    print(n)
    show(n - 1)
    print(n)

show(2)


# def show(2):
#     if 2 == 0:
#         print("Stop")
#         return

#     print(2)   #2
#     show(2 - 1)   #1
#     print(n)

# show(2)


# def show(1):
#     if 1 == 0:
#         print("Stop")
#         return

#     print(1)   #1
#     show(1 - 1)   #0
#     print(n)

# show(2)


# def show(0):
#     if 0 == 0:
#         print("Stop")
#         return

#     print(1)   #1
#     show(1 - 1)   #0
#     print(n)

# show(2)


#output
#2
#1
#Stop
#1
#2


#Q2
def total(n):
    if n == 0:          #this is the base case that stops the loop 
        return 0

    return n + total(n - 1)


#when the n has value are o then the it return the o and the below code od the return are not executed there so base case are important at there


#Q3
def count(n):
    if n == 0:
        return

    count(n + 1)


#rewrites
def count(n):
    if n == 0:
        return

    count(n - 1)        #the n+1 always increase the n count so it dont reach at the end of the loop  so we need the - aign imnstant of the +sign there
print(count(2))



#Q4
def answer(n):
    if n == 0:
        return 0

    return n + answer(n - 1)

print(answer(3))

#firstly it reaise the error beacure there the return are not wrriten and at gait the none type so we cant add the none and the int ,so we need the return statmetn tere so etun the 6 at there


#Q5
def coutn_down(n):
    if n==0:
        return "done"
    # return coutn_down(n-1)
    print(n)
    return coutn_down(n-1)

print(coutn_down(3))


#Q6
def count_def(n):
    if n==0:
        return 0
    count_def(n-1)
    print(n)
count_def(4)


#Q7
def sum_to(n):
    if n==0:
        return 0
    return n + sum_to((n-1))
print(sum_to(5))



#Q8

def factorial(n):
    if n<=1:
        return n
    return n* factorial(n-1)
print(factorial(5))



#Q9
def digit_sum(n):
    if n==0:
        return 0
    return n+ digit_sum(n-1)
print(digit_sum(5))



#Q10
def power(base,exponent):
    if exponent==0:
        return 1
    return base * power(base,exponent-1)
print(power(2,5))
print(power(9,0))



#Q11
count=0
def count_digits(n):
    global count
    if n<10:
        count+=1
        return count
    count+=1
    return n%10 +count_digits(n//10)
count_digits(534582)
print(count)


#Q12
def reverse_text(text):
    if text == "":
        return ""
    return text[-1] + reverse_text(text[:-1])
print(reverse_text("cat"))


#Q13
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(1))


#Q14
maximum=0
def max_digit(n):
    global maximum
    if n==0:
        return maximum
    if n%10>maximum:
        maximum=n%10
    return max_digit(n//10)
max_digit(9728)
print(maximum)


#Q15
def mystery(n):
    if n <= 1:
        return n
    return mystery(n - 1) + mystery(n - 2)
print(mystery(4))       

#output
#3


#Q16
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
print(factorial(5))


#Q17
def stop_at_zero(n):
    if n == 0:
        return

    stop_at_zero(n-1)
print(stop_at_zero(4))


#Q18
#If a recursive function makes too many nested calls, Python may run out of recursion depth and stop executing.
#- Error: RecursionError
#- Why use a loop? A loop is better for very large counting tasks because it avoids creating too many nested function calls and uses less memory.
