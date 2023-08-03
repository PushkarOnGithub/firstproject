"""print('happy diwali')"""
# happy diwali
# escape characters \r \n \t \b
"""print("pushkar iss\r a good boy")"""
# variables #datatypes= str, int ,float...
var1 = "pushkar37"
print(var1)
varbhatka = "Bhanu pratap saini"  # str datatype
print(varbhatka)
var2 = 6  # int datatype
print(var2)
var3 = 34.9  # float datatype
print(var3)
# type function
print(type(varbhatka))
print(type(var3))
var4 = "56"
# typecast = changing type of datatypes #simple algebra bw variables #.isnumeric() #.isalnum() #.isalpha()
print(var1+str(var2))
print(str(var4) + str(var2))
var5="deepti\n"
print(2*(var5))
print(var4.isnumeric())  # checks if the 'string' only contains number valus without spaces
print(varbhatka.isalpha())  # checks if the 'string' only contains letters without spaces
print(var1.isalnum())  # this is the mixture of isnumeric and isalpha
# take input from user
"""print("enter your number")
impnum = input()
print("you entered",int(impnum))"""
# in print function if we use comma it will take input as 'str' but if we use '+' to add the inputs it will take input as it is.
# as in above example if we use print("you entered"+int(impnum)+10). it will show error. correct should be print("you entered"+str((int(impnum)+10)))
# I made a adder

# String methods

# strings #string slicing #len fuction
mystr = "pushkar is a good boy"
print(mystr)
print(mystr[0:8])
print(mystr[0:8:4])
print(len(mystr))
print(mystr[:14])  # consider 0 on the left side if left blank
print(mystr[:])  # consider length of str if left blank on the right side
print(mystr[::])  # consider 1 on the rightmost side if left blank
print(mystr[:-3])  # in case of negative numbers count from last
print(mystr[::-1])  # here it will reverse the string
print(mystr[::-3])  # here it will first reverse the string and then apply the required gap
# some functions
# .endswith() #.isalpha() #.isalnum() #.count() #.capitalize() #.find() #.lower() #.upper() #.replace()
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.title())  # makes the string look like a title i.e. each word is seperately captalised
print(mystr.capitalize())  # only first letter will be capatilized
print((mystr.capitalize).swapcase())
print(mystr.find("bo", 0))  # returns the lowest index of occurence found. an optional argument can be passed to start searching after a particular index
print(mystr.rfind("bo", 0))  # returns -1 if not found

print(mystr.upper())  # capitalize whole string

print(mystr.replace("is","are"))  # removes all the occurences of the first argement with second argument

print(("      " + mystr + "   ").strip())  # strip removes all the whitespaces at end and start of the string
print(("##" + mystr + "####").strip("#"))  # if an argument is passed in the strip it will remove that character instead of whitespaces now
print("www.example.com".strip("wcom."))   # if multiple characters are passed then it will remove all the occurences of them from string
print(("    " + mystr + "   ").rstrip())  # rstrip() starts striping from right leaving left side unchanged
print(("    " + mystr + "   ").lstrip())  # lstrip() starts striping from left leaving right side unchanged

print(("Hello Dear: " + mystr).removeprefix("Hello Dear: "))  # removeprefix() removes passed argument as prefix
print((mystr + "Bye Dear: ").removesuffix("Bye Dear: "))  # removesuffix() removes passed argument as suffix
# re.sub
print(mystr.split())  # split returns a list containing all elements seperated by a delimiter
print(mystr.split(',', maxsplit=1))  # maxsplit: maximum splits=1 (here)

print(mystr.partition('is'))  # returns a tuple. it partitions a string into three parts being passed argument in the middle. if not found last two elements are empty strings

print(mystr.center(50, '-'))  # makes a new string with given length by filling passed character on each sides
print(mystr.ljust(50, '-'))  # it will just fill the character from right side meaning string will be in left
print(mystr.rjust(50, '-'))  # it will just fill the character from left side meaning string will be in right

print("42".zfill(5))  # makes a number in the string of required length. sign will count as a character

# list=[] #.sort() #.reverse() #list slicing #.append() #.pop()
syllabus = ['physics', "chemistry", "maths", "english"]
print(syllabus)
print(syllabus[3])
numbers = [2, 4, 9, 2]
print(numbers[3])
numbers.sort()  # arranges elements in ascending order
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[:])
print(numbers[:3])
print(numbers[::4])
syllabus.append("hindi")  # append adds element in list
print(syllabus)
syllabus.insert(1,8)  # insert takes first input as index of the element at which we wish to insert and second as the data
print(syllabus)
syllabus.remove(8)
print(syllabus)
syllabus.pop()  # pop will chop off the last element of the list
print(syllabus)
# some advanced functions
# to change value of a list's element #mutable=can change #immutable
# tuples=():immutable list with paranthesis  #lists are mutable
numbers[2] = 67  #it will change the value of first '2' it will find in the list to 67
print(numbers)
tp = (2, 3, 5)
# to swap the values of two variables
# classic method
a = 1
b = 5
temp = a
a = b
b = temp
print(a, b)
# in python modern method
c = 2
d = 7
c, d = d, c
print(c, d)
# dictionary={} ;dictionary is nothing but key value pairs arrenged in a sequence
# del dict[] #.copy() #.get() #.update()
d1 = {}
d2 = []
d3 = ()
print(type(d1))
print(type(d2))
print(type(d3))
d4 = {"pushkar": "pk", "lokesh": "helicopter", "neeraj": "dhuko", "kuldeep": {"main": "chatta", "temporary": "gosai"}}
print(d4["pushkar"])  # ##case sensitive
print(d4['lokesh'])
print(d4["kuldeep"]["main"])
d4["saurabh"] = "solanki"  # updating the dict
print(d4)
del d4["kuldeep"]         # deleting from list
print(d4)
d5=d4.copy()      # we should use copy function so that the parent dict is unaffected
print(d5)
print(d4.get("pushkar"))  # get is preferred as it will return 0 if element is not found not an error like other methods
d4.update({"ajay":"bhoja"})
print(d4)
print(d4.keys())
print(d4.items())  # Returns a list containing a tuple for each key value pair
# exercise1 = done in first attempt

# sets #make set from list/tupal
# .add() #.remove() #.union() #.intersection()
s = set()
print(type(s))
setfromlist = set([1, 2, 3, 4])
print(setfromlist)
s.add("halloween")
print(s)
s1 = s.union({1, 2, 4, 3})
print(s1)  # all set operations are same as they were in mathematics

# if..else function
print(var1, var2, var3, var4, var5)
"""print("enter your number")
var6 = int(input())
if var6>var2:
    print("this number greater than 6")
if var6==var2:                    #in place of 'if','elif' can also be used as a second if statement but if 'if' gets already true it will not check elif code
    print("this numbers is 6")
else :
    print("this number is lesser than 6")"""
#'in' keyword #'not in' keyword
if "physics" in syllabus:
    print("yes its in the list")

#for loop function #.items()
list1=["eyes","ears","nose","tongue","skin"] #tupal can also be used in place of a list
for item in list1:
    print(item)
list2=[["harry",1],["larry",2],["carry",6],["marie",250]]
for item in list2:
    print(item)
for item,lollypop in list2:
    print(item,lollypop)
dict1=dict(list2)
print(dict1)
for item,lollypop in dict1.items():
    print(item,"eats",lollypop,"lollypop")
for item in dict1:    #it will only print keys of the dictionary
    print(item)
for item in list1:
    if len(item)<5:
        print(item)
for item,lollypop in list2:
    if lollypop<5:
        print(item)
#while loops
"""i=0
while(i<5):
    print(i)
    i=i+1"""
#break and continue
"""p=0
while(True):
    print(p,end=" ")
    if (p==44):
        break
    p=p+1"""
"""q=0
while(True):
    if q+1<5:
      q=q+1
      continue
    print(q,end=" ")
    if (q==44):
        break
    q=q+1"""


# quiz4 #exercise3

# opertators in python

# arithmatic operators = (+,-,*,/,//,**,%) ##(//)=greatest integer function ##(**)=power ##(%)remainder
print("greatest integer of 45/4",45//4)
print("2 raised to the 10 is",2**10)
print("remainder after divison 45/4",45%4)

# assignment operators=(+=,-=,/=,*=,%=.....)
x = 6
x *= 2
print(x)
x %= 5
print(x)

# comparision operators=(==,!=,<,>,<=,>=...)

# logical operators=(and(&),or(|),not...) #mathematical reasoning
m = True
n = False
print(m and m, m and n, n and n)

# identity operators=(is,is not)
print(m is n, m is not n)

#membership operators=(in,not in)
if "physics" in syllabus:
    print("yes its in the list")

# bitwise operators=(0=00,1=01,2=10,3=11)
# see bits vertically to do calculation
print(1 & 0)
print(3 & 0)
"""3=11
     👇👇 
    0=00
     👇👇
      00=0
           """
print(1 | 0)
# shorthand if else
"""a=int(input("enter a"))
b=int(input("enter b"))
print("b a se bada hai bhai") if b>a else print("a b se bada hai bhai")"""
# functions #builtin functions #userdefined functions #doc string(.__doc__)=First string typed in a function.
                                                            # Generally we write it to remember the working of function
s = sum((a,b)) # builtin functions

# ASCII functions 
aa = ord("a")  # to get the ASCII value of the character passed
print(aa)
aa2 = chr(aa)
print(aa2)  # to convert the ASCII into character

def function1():
    print("hello you are in function 1")    # userdefined function
function1()
def average(a, b):
    """this function will calculate the average of two numbers"""
    print("average of the numbers is", (a + b)/2)
average(4, 5)
print(average.__doc__)  # dont use parenthesis after function to access the doc string of the function

# try except handling = used when code shows error but we want to also run the code which is not showing error
"""x=input("type x:")
y=input("type y:")
try:
    print(int(x)+int(y))
except Exception as e:
    print(e)
"""
# file IO basics
"""                                  #read and text mode are default
"r" : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
"w" : w mode does not concern itself with what is present in the file.
      It just opens a file for writing and if there is already some data present in the file, it overwrites it.
"x" : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
"a" : a stands for append, which means to add something to the end of the file. It does exactly the same.
      It just adds ;the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file.
      It also does not have the permission of reading the file.
"t" : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string.
"b" : b stands for binary and this mode can only open the binary files, that are read in bytes.
      The binary files include images, documents, or all other files that require specific software to be read.
"+" : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file."""
# reading a file
f = open("practice.txt", "rt")        # file handle/pointer #open takes first argument as the directory of the file and second as the mode
content = f.read(16)                 # once read all the data is in 'content' not in 'f' #continuously read the file as the argument says
                                     # if no argument given it will take the whole document as the argument
print("1", content)
content = f.read(64)
print("2", content)
content = f.read(256)                # this will read nothing as the complete file has been read already
print("3", content)

f.close()                            # don't forget to close the file as soon as the work with the file is completed
f = open("practice.txt", "rt")
for line in f:
    print("4", line, end="")           # i have added the end=..... to read the whole line not character by character
f.close()
f=open("practice.txt")
print("5", f.readline())              # it will read only the first line in the file
print("6", f.readline())              # it will read only the second line in the file and so on...
f.close()
f = open("practice.txt", "rt")
print("7", f.readlines())             #.readlines() will convert the data into a list
f.close()
#writing/appending a file
"""f = open("practice2.txt","Water")
f.write("This world is becoming out of control") #it will rewrite the file with the argument
f.close()"""
"""f = open("practice3.txt","a")
f.write("This world is becoming out of control") #it will add the argument in the end of the file as many times it runs
f.close()"""
"""f = open("practice3.txt","Water")
a = f.write("This world is becoming out of control")
print(a)                                              #by this you can have the number of characters written/appended 
f.close()"""

# handle read/write both
"""f = open("practice3.txt","r+")
print(f.read())
f.write("thanks")"""
# exercise4
# more operations on files
"""f = open("practice2.txt")
print(f.tell())                #.tell() will inform us about at which index it is working in the document
print(f.readline())
f.seek(11)                     #.seek() will seek the document to the index as given in argument.it will start reading from there
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())

f.close()"""

# with block to open files
"""with open("practice2.txt") as f:               #this open block works same as above but now we don't have to close file
    print("8",f.readlines())
"""

# Global variables #local variables
"""l=10                  #global variable:they can be used anywhere in the file
m=10
def function1(n):
    l=5               #local variable:they are defined for a small scope and can only be used there,like l has value of 5 only in function1()
                      #here l is read only variables we can not change its value while being in a local scope
                      #only local variables can be changed in local scope
    global m          #but if we strongly want to change the value of a global variable while being in a local scope we have to use 'global' keyword
    m=m+5
    print(n,l,m)
function1("hello there") #program always looks firstly in local scope then in global

#Recursions : when we use a function again and again to complete the task
#factorial using recursions
n=int(input("input a number to calculate factorial\n"))
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(str(factorial(n)).count("0"))
print(str(factorial(n)).count("1"))
print(str(factorial(n)).count("2"))
print(str(factorial(n)).count("3"))
print(str(factorial(n)).count("4"))
print(str(factorial(n)).count("5"))
print(str(factorial(n)).count("6"))
print(str(factorial(n)).count("7"))
print(str(factorial(n)).count("8"))
print(str(factorial(n)).count("9"))
"""
# Fibonacci's numbers
"""n=int(input("enter n to calculate nth Fibonacci number:\n"))
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))"""

# Lambda function or anonymous function: function banane ka short tarika

"""minus = lambda x,y: x-y    this lambda function is equivalent to: def minus(x,y):
                                                                        return x-y"""
import random
list3 = ['my',"name","is", "pushkar"]
print(random.randrange(3, 9, 2))  # #start , stop , step
print(random.randint(1, 5))      # #start , stop+1
print(random.choice(list3))   # select an element at random from given array,str...
print(random.choices(list3, weights = [1, 2, 3, 4], k = 2))    # ruturns a list with full control

                # random.shuffle() modifies elements in a random order
                # random.random() returns a float bw 0 and 1
                # random.sample() returns a sample of the given data
                # .uniform() returns a float bw two given numbers

## F-strings and string formatting

u = "this is {}"
v = "this is {1} {0}"
me = "Pushkar"
au = u.format(me)
print(au)
av = v.format(var1,me)
print(av)

aw = f"this is {me} {150*20}"
print(aw)

# #time module

import time
curr = time.time()   # #time.time() returns seconds since epoch
print(curr)
# exercise.ArmstrongNumbers()
# time.sleep(2)       ##delays the execution of the program further
print(time.ctime())  # #time.ctime() takes number of seconds passed since epoch and returns local time
# #time.struct_time
print(time.localtime(1637465346))  # #localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.
print(time.asctime(time.localtime(time.time())))         # #same as time.ctime()
print(f"This time program took {time.time() - curr} seconds to complete")

## *args and **kwargs
def funargs(normal_argument, *args, **kwargs):                ##args and kwargs can be used to give input to a function as a tuple
    print(normal_argument, "This was the normal argument")
    for i in args:
        print(i, end=" ")

list4 = ["1", "2", "3", "4", "5"]
funargs("Bahut Khoob", *list4)

## virtual environment and requirements.txt

# virtual environments are used to freeze the code itself, means it can be accessed at any time in the future. By creating a vir-env we are basically creating a clone of the
#Interpreter

#to install virtual environment in terminal(admin) write 'pip install virtual env'
# to create a vir-env write 'virtualenv {name of env say ps}
# to activate the vir-env write '.\ps\scripts\activate
# to deactivate simply write 'deactivate'
# we can install modules in the vir-env itself it won't affect the original interpreter
# to export requirements for the code in a txt file write 'pip freeze > requirements.txt'
# to install modules requirements, go to the folder of requirements.txt and write in windows terminal 'pip install -r .\requirements.txt' press enter
# to create a vir-env with the site package already installed write 'virtualenv --system-site-packages {name of vir-env}'

## Enumerate Function can be used to return the index,element at the same time. No mannual indexing is required

for i,j in enumerate(list4):
    if i%2 == 0:
        print("\n",j)

## we can import one python file into another file by using import
# but if we import directly the file the imported file will run as it is as a whole
# so we have to use if __name__ = __main__ before the execution part of the program so that the program itself run as it is as well as
# it can be used in another program by using import without the whole execution.
# the value __name__ is __main__ if the program runs itself but if it imported into another the value of __name__ changes to the name of the program
# hence it can not be used outside the program itself.

## Join Function

joined = " and ".join(list4)
print(joined)

## map filter reduce

print(list4)
intOFlist4 = list(map(int,list4))         #map runs a function to a datatype(list,tuple...)
print(intOFlist4)

sqOFlist4 = list(map(lambda x:x**2 , list(map(int,list4))))
print(sqOFlist4)

def sq(a):
    return a**2
def cub(b):
    return b**3
listOFfunc = [sq,cub]
for i in range(7):
    sqANDcube = list(map(lambda x:x(i), listOFfunc))
    print(sqANDcube,end=" ")

##filter

filtered = list(filter(lambda a:a>3, intOFlist4))     ##filter runs given function to the iterable and returns the elements of iterable which returned true in function
print(filtered)
##reduce
from functools import reduce

sumTILL7 = reduce(lambda a,b: a+b, range(8))       ##reduce runs given function to given iterable and returns reduced value ex. reduce(sum,[a,b,c]) = ((a+b)+c)
print(sumTILL7)

# Decorators in python : they reduce repeatability of the code by working as a template

# classes are like a templates for objects so that we don't have to repeat a particular section of code. Objects fill the classes.

class Students1():
    pass

pushkar = Students1()

rahul = Students1()
rahul.name = "Rahul Kumar"
rahul.education = "B.Tech"

print(rahul)
print(Students1)
print(Students1)

class Students():
    Age_of_students = 15                    # First it will search in instance variables for a value, if not found then it will take class variable
    def __init__(self,name1,education1):    # Constructor : to give arguments to the class rather than giving them manually
        self.name = name1
        self.education = education1
    def pk(self):
        return f"{self.name} you were in function pk"

pushkar = Students("Pushkar Saini","12th")   #passing arguments to __init__ function
mudit = Students("Mudit Pathak","B.Tech")
print(pushkar.name)
print(pushkar.education)
print(pushkar.__dict__)
print(Students.Age_of_students)              #if we change Students.Age_of_students it will be changed for all objects of class
print(pushkar.Age_of_students)               #but if we change pushkar.Age_of_students it will be changed for only the perticular object of the class, a copy of the variable is created in the memory

pushkar.Age_of_students = 16
print(pushkar.Age_of_students)
print(Students.Age_of_students)
print(Students.__dict__)

print(pushkar.pk())
print(mudit)

class Students2():
    no_of_holidays = 30
    def __init__(self, name, presents, absents):
        self.name = name
        self.presents = presents
        self.absents = absents

    @classmethod                               # class methods are used when we want to access class varibles without passing self
    def change_holidays(cls, newholidays):     # class methods can be used when we don't want to pass self as a argument.
        cls.no_of_holidays = newholidays

    @classmethod                               # class methods as alternative constructors
    def objectfromstr(cls, string):
        elements = string.split("-")
        return cls(elements[0], elements[1], elements[2])

    @classmethod
    def objectfromstrAlternate(cls, string):
        return cls(*string.split("-"))

    @staticmethod                              # static methods are used when we want to define a function for the class. it will run on objects and class
    def printgood(string):
        print("This is good ", string)



pks = Students2("pushkar",150,50)
print(Students2.no_of_holidays)
Students2.change_holidays(35)
print(Students2.no_of_holidays)

# class methods as alternate constructors

prince = Students2.objectfromstr("Prince-160-30")
print(prince.name)
nayan = Students2.objectfromstrAlternate("Nayan-140-40")
print(nayan.absents)

# static methods
nayan.printgood("hello")
Students2.printgood("jeelo")


