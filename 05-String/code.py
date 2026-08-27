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