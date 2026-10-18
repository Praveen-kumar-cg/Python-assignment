#6. Practice Problems

#Q1
def welcome():
    print("welcome to python")

welcome()
welcome()
welcome()

#Q2
def greet(name):
    print(name)
greet("praveen")


#Q3
def show_number(number):
    print(number)
show_number(29)


#Q4
def add(a, b):
    return a+b
print(add(10,20))


#Q5
def square(number):
    return number*number
print(square(2))


#Q6
def is_even(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
print(is_even(12))


# Q7
def get_full_name(first_name, last_name):
    return first_name +last_name
print(get_full_name("praveen","bishnoi"))


# Q8
def introduce(name, city="Pune"):
    return name,city
print(introduce("praveen"))
print(introduce("praveen","saanchore"))



# Q9
def subtract(a, b):
    return a-b
print(subtract(10,5))
print(subtract(5,10))


# Q10
def get_min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a

print(get_min_max(10, 5))
print(get_min_max(3, 8))


# Q11
def calculate(a, b):
    return a+b,a-b,a*b,a/b
print(calculate(10,20))

# Q12
def count_digits(number):
    count=0
    while number>0:
        digit=number%10
        count+=1
        number=number//10
    return count
print(count_digits(1234))


# Q13
def  classify_number(number):
    if number>0:
        return "positive"
    elif number==0:
        return "zero"
    else:
        return "negative"
print(classify_number(21))


# Q14 
def calculate_total(price, quantity=1):
    return price*quantity
print(calculate_total(12,4))


# Q15
def create_email(username, domain="example.com"):
    return username+domain
print(create_email("praveen.bishnoi.cg"))


# Q16
def format_name(first, last, uppercase=False):
    if uppercase==True:
        full=(first+" "+last).upper()
        return full
print(format_name("praveen","bishnoi",True))


# Q17
def percentage(marks, total=100):
    return (marks/total)*100
print(percentage(99))


# Q18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes*seconds_per_minute
print(convert_minutes(2))

# Q19
def student_details(name, age, city):
    return name,age,city
print(student_details(age=18,city="snachore",name="praveen bishnoi"))


# Q20
def bill(item, quantity=1, price=100):
    return item,quantity,price
print(bill("laptop",price=1415252,quantity=1))


# Q21
def analyze_number(number):
    if number < 0:
        absolute = -number
    else:
        absolute = number

    if number % 2 == 0:
        even = "even"
    else:
        even = "odd"

    count = 0
    temp = absolute

    if temp == 0:
        count = 1
    else:
        while temp > 0:
            digit = temp % 10
            count += 1
            temp = temp // 10

    return absolute, even, count


print(analyze_number(1242))
print(analyze_number(-135))
print(analyze_number(0))




# Q22
def calculate_stats(a, b, c):
    if a>b and a>c:
        largest=a
        if b>c:
            smallest=c
        else:
            smallest=b
    elif b>c and b>a:
        largest=b
        if c>a:
            smallest=a
        else:
            smallest=c
    elif c>a and c>b:
        largest=c
        if a>b:
            smallest=b
        else:
            smallest=a
    return largest,smallest,a+b+c
print(calculate_stats(1,2,3))




# Q23
def make_sentence(subject, verb, object):
    return subject+" "+verb+" "+object
print(make_sentence(verb="reads",object="a book",subject="She"))


# Q24
def apply_discount(price, discount=0):
    return price-discount
print(apply_discount(price=12415,discount=2415))


# Q25
def calculate_pay(hours, rate=200, bonus=0):
    return (hours*rate)+bonus
print(calculate_pay(12,bonus=1234,rate=250))



# Q26
def get_coordinates(x=0, y=0):
    return x,y
print(get_coordinates())
print(get_coordinates(y=12))




# Q27
def compare(a, b):
    if a>b:
        largest="A is greater"
        difference = a - b
    elif a<b:
        largest="B os greater"
        difference = b - a
    else:
        largest="equal"
        difference = 0
    return largest,difference
print(compare(2,3))


# Q28
def convert_temperature(value, scale="C"):
    if scale=="c":
        fahrenheint=((9/5)*value)+32
        return fahrenheint
    if scale=="f":
        celsius=(value - 32) * 5 / 9
        return celsius

print(convert_temperature(30,"c"))


# Q29
def calculate_result(marks, passing_marks=35):
    if marks>passing_marks:
        return "pass"
    else:
        return "fail"
print(calculate_result(67))



# Q30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return item,(quantity*price)+delivery_fee
print(order_summary("laptop",2,200000,delivery_fee=200))