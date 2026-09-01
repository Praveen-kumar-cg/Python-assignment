#Part 3 — String Creation and Basic Operations
#Task 1 — Create Strings
your_name="Praveen"
your_city='Sanchore'
favorite_language='Python'
massage="my name is praveen kumar \n form sanchore rajasthan and \n i am btech cse student at coding gita"
print("Output for task-1......................................")
print(your_city,your_name,favorite_language,massage)

#Task 2 — Empty String
name=""
print("Output for task-2......................................")
print(name,"length of string=",len(name),type(name))

#Task 3 — String Information
a="Python Programming"
print("Output for task-3.......................................")
print(a)
print(len(a))
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])

#Part 4 — Indexing
#Task 4 — Positive Indexing
A="Programming"
print("Output for task-4.......................................")
print(A[0])
print(A[1])
print(A[4])
print(A[-1])


#Task 5 — Negative Indexing
A="Programming"
print("Output for task-5.......................................")
print(A[-1])
print(A[-2])
print(A[-3])
print(A[-11])

#Task 6 — Indexing Challenge
name="Praveen Kumar"
print("Output for task-6.......................................")
print(name[0])
print(name[-1])
print(name[8])

#Part 5 — Slicing
#Task 7 — Basic Slicing
b="Python Programming"
print("Output for task-7.......................................")
print(b[:6])
print(b[7:])
print(b[:])
print(b[0:6])
print(b[-5:])

#Task 8 — Slicing with Step
z="ABCDEFGHIJKL"
print("Output for task-8.......................................")
print(z[::2])
print(z[::3])
print(z[1:9:2])
print(z[::-1])

#Task 9 — Slicing with Negative Indexes
q="Python Programming"
print("Output for task-9.......................................")
print(q[-5:])
print(q[-10])
print(q[::-1])

#Task 10 — Slicing Challenge
s="Praveen kumar"
print("Output for task-10.......................................")
print(s[:4])
print(s[-3:])
print(s[::2])
print(s[::-1])
print(s[1:12])

#Part 6 — Length
#Task 11
x="Praveen kumar"
y="""My name is praveen kumar and
i am btech cse student at coding gita swaminarayan university"""
z='''helloo    everyone your welocme to coding gita swaminarayan university'''
print("Output for task-11.......................................")
print(len(x))
print(len(y))
print(len(z))

#Task 12
text = "Python Programming"
print("Output for task-12.......................................")
print(len(text))
print(text[len(text)-1])

#Part 7 — Concatenation
#Task 13 — Full Name
first_name="Praveen"
last_name="Kumar"
print("Output for task-13.......................................")
print(first_name+" "+last_name)

#Task 14 — Sentence Creation
name="praveen kumar"
age="18"
city="Sanchore"
language="Python"
print("Output for task-14.......................................")
print(name+" "+age+" "+city+" "+language)


#Task 15 — String and Integer
name="Praveen"
age=18
age=str(age)
print("Output for task-15.......................................")
print("Python show:--TypeError: can only concatenate str (not int ) to str")
print(name+" "+age)

#Part 8 — String Repetition
#Task 16
x="hello"
print("Output for task-16.......................................")
print(x*3)
print(x*5)
print(x*10)

#Task 17 — Pattern
a="*"
print("Output for task-17.......................................")
print(a*10)

#Part 9 — Case Conversion
#Task 18
x="python programming language"
print("Output for task-18.......................................")
print("upper:-",x.upper())
print("lower:-",x.lower())
print("capatalize:-",x.capitalize())
print("title:-",x.title())
print("swapcase:-",x.swapcase())

#Task 19 — Case-Insensitive Comparison
x="Python"
y="python"
print("Output for task-19.......................................")
print(x==y)
x=x.lower()
print(x==y)

#Part 10 — Searching
#Task 20 — Membership
x="Python is a programming language"
print("Output for task-20.......................................")
print("Python" in x)
print("programming" in x)
print("Java" in x)
print("language" in x)

#Task 21 — find()
x="Python is a programming language"
print("Output for task-21.......................................")
print(x.find("Python"))
print(x.find("programming"))
print(x.find("language"))
print(x.find("Java"))

#Task 22 — index()
x="Python is a programming language"
print("Output for task-22.......................................")
print(x.index("Python"))
print(x.index("programming"))
print(x.index("language"))
print("print(x.index(Java)) show the :-ValueError: substring not found")

#Task 23 — Count Characters
a="banana"
print("Output for task-23.......................................")
print(a.count("a"))
print(a.count("n"))
print(a.count("b"))

#Task 24 — Starts and Ends
filename = "student_notes.pdf"
print("Output for task-24.......................................")
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))


#Part 11 — Replacing
#Task 25 — Replace a Word
text = "I am learning Java"
print("Output for task-25.......................................")
print(text.replace("Java","Python"))


# Task 26 — Multiple Replacements
text = "apple apple apple"
print("Output for task-26.......................................")
print(text.replace("apple","mango"))


#Task 27 — Limited Replacement
text = "apple apple apple"
print("Output for task-27.......................................")
print(text.replace("apple","mango",1))


#Task 28 — Check Immutability
text = "Python"
b=text.upper()
print("Output for task-28.......................................")
print(b)
print(text)
text=text.upper()
print(text)

#Part 12 — Whitespace
#Task 29
text = "   Python Programming   "
print("Output for task-29.......................................")
print("strip-",text.strip())
print("lstrip-",text.lstrip())
print("rstrip-",text.rstrip())

#Task 30 — User Input
# x=input("enter your name:-")
print("Output for task-30.......................................")
print(x.strip())

#Part 13 — Split and Join
#Task 31 — Split
a="Python is easy to learn"
print("Output for task-31.......................................")
print(a.split())

#Task 32 — Split with Separator
x="apple,banana,mango,orange"
print("Output for task-32.......................................")
print(x.split(","))


#Task 33 — Join
words = ["Python", "is", "easy"]
print("Output for task-33.......................................")
print(" ".join(words))

#Task 34 — Join with Different Separators
word=["Python","is","easy"]
print("Output for task-34.......................................")
print("-".join(word))
print("/".join(word))


#Part 14 — String Formatting
#Task 35 — F-String
name="praveen kumar"
age=18
city="sanchore"
print("Output for task-35.......................................")
print(f"My name is {name} and my age is {age} and i am from {city}")


#Task 36 — Arithmetic Inside F-String
a = 10
b = 20
c=a+b
print("Output for task-36.......................................")
print(f"The sum is {c}")

#Part 15 — Error Identification
#Task 37
print("Output for task-37.......................................")
print("IndexError: string index out of range")
text = "Python"
print(text[2])
print("TypeError: 'str' object does not support item assignment,python string is immutable")
text = "Python"
print("J"+text[1:])
print("TypeError: can only concatenate str (not int) to str,python is case sensetive so we can tadd them also we cant add the string and integer directy python show error")
age = 20
print(age + age)
print("ValueError: substring not found,index show error when string is not found in the variable")
text = "Python"
print(text.index("Python"))

#Part 16 — Practical Challenge
#Task 38 — Name Processor
# name=input("Enter your full name:-")
print("Output for task-38.......................................")
name1=name.strip()
print("Original name:-",name)
print("cleaned name:-",name1)
print(name1.upper())
print(name1.lower())
print(name1.title())
print(len(name1))
print(name1[0])
print(name1[-1])
print("a" in name1)

#Part 17 — Practical Challenge
#Task 39 — Sentence Analyzer
data=input("Enter briff about python:-")
print("Output for task-39.......................................")
print(data)
print(len(data))
l1=data.split()
print(len(l1))
print(l1[0])
print(l1[-1])
print(data.upper())
print(data.lower())
print(data.title())
print("Python" in data)
d=data.title()
print(data.count("Python") or d.count("Python"))

#Part 18 — Final Challenge
#Task 40 — Student Information
print("Output for task 40:.................................................")
your_fname=input("Enter your First name:-")
your_lname=input("Enter your Last name:-")
your_city=input("Enter your City:-")
your_course=input("Enter your Course:-")
your_age=(input("Enter your age:-"))

#1
print(your_fname.strip(),your_lname.strip(),your_city.strip(),your_course.strip(),your_age.strip())
#2
fullname=your_fname+" "+your_lname
print(fullname)

#3
print(fullname.title())

#4
print(fullname.upper())

#5
print(fullname.lower())

#6
length=len(fullname)
print(length)

#7
print(fullname[-length])

#8
print(fullname[length-1])

#9
print(your_city,"and",your_course)

#10
print(f"my age is {your_age}")

#11
print("Python" in your_course  or "Python" in your_course.title())

#12
tyour_course=your_course.title()
print(tyour_course.replace("Python","Java"))

#13
list=your_course.split()
words=len(list)
print(words)