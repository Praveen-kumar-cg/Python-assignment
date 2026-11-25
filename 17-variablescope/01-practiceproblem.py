# 12. Practice Problems

# Q1
def find():
    city="sanchore"
    print(city)
find()

# Q2
school="jnv"
def findschool():
    print(school)
findschool()


# Q3
if 2<4:
    ageOf=19
print(ageOf)


# Q4
for i in range(5):
    pass
print(i)


# Q5
#scope= scoping means that the where we can access the variable
#lifetime=variable lifetime means that how long tha variable binding are exist 


# Q6
value = 100
def test():
    value = 200
    print(value)
test()
print(value)

#output
#200
#100


#Q7
clicks = 0
def click():
    global clicks
    clicks += 1


# Q8
name = "Asha"
def show():
    print(name)
    name = "Ravi"
show()

#it shows the locan unbound error because the printing the name variable before the assigning in the local so it cant ge the valuse from the global


#Q9
name="outer"
def outter():
    name="enclosing"
    def inner():
        print(name)
    inner()
outter()





# Q11
def outter():
    count=0
    def inner():
        nonlocal count
        count+=1
        return count
    return inner
count=outter()
print(count())
print(count())
print(count())


# Q12
x=1
def outer():
    x=2
    def inner():
        x=3
        print(x)
    inner()
    print(x)
outer()
print(x)



# Q13

#In Python, normal for loops do not create a separate scope, but list comprehensions create their own scope in Python 3


Q14
def outter():
    count=0
    def inner():
        nonlocal count
        count+=1
        return count
    return inner
count=outter()
print(count())
print(count())
print(count())



#Q15
 #because they are the inbuilt function and if the any variable is not found then the it search for the inbulid so be avoid to use the inbuild function anme for the variable name