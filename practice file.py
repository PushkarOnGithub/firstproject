"""list1=["eyes","ears","nose","tongue","skin"]
list2=[["harry",1],["larry",2],["carry",6],["marie",250]]
for item in list1:
    if item.endswith("e"):
        print(item)
    if len(item)<5:
        print(item)
for item,lollypop in list2:
    if lollypop<5:
        print(item)
var1=2

var2="2"
var3="pushkar"
print(var2.isalpha())
n = int(input())"""
import sys

"""n = int(input("input a number\n"))
def numtype(o):
    p = o/2
    q = p.is_integer()
    if q == True:
        return "even"
    else:
        return "odd"

if numtype(n) == "odd":
    print("Weird")
elif numtype(n) == "even" and 2<=n<=5:
    print("Not Weird")
elif numtype(n) == "even" and 6 <= n <= 20:
    print("Weird")
elif numtype(n) == "even" and 20 <= n <= 100:
    print("Not Weird")"""
"""nums = [2,7,11,15]
target = input("k\n")
def indices(target):
            if x+y==target:
                return (nums.index(x),nums.index(y))
            else:
                return "try again"
print(indices(target))
"""

"""list2=[["harry",1],["larry",2],["carry",6],["marie",250]]
list2.sort()
print(list2)"""

###summation of 1/n series till n terms
"""sys.setrecursionlimit(100000)
n= int(input("input a no."))
def srs(n):
    if n==1:
        return 1
    else:
        for n in range(1,n+1):
            m = float(n)
        return (1/m) + srs(n-1)
print(srs(n))
"""
### tables
"""n=int(input("type number to generate table\n"))
def tables(n):
    o = (n*10)+1
    p = range(0, o, n)
    for i in p:
        print(i)
tables(n)"""
"""def determinant(a,b,c,d,e,f,g,h,i):
    o = (a*e*i - a*h*f - b*d*i + b*f*g + c*d*h - c*g*e)
    return o
print(determinant(2,-3,1,2,0,-1,1,4,5))"""


##find the prime number
"""num = int(input("input the number to check prime\n"))
div = 2
while div < num :
    if num%div == 0:
        print("not prime")
        break
    else:
        div = div + 1
if div == num:
    print("prime")"""


##find all prime numbers till a number

"""num = int(input("input the number to get prime numbers till the number\n"))
#num2 = 2
div = 2
while div < num :
    if num%div == 0:
        continue
    else:
        print(div)
        div = div + 1
if div == num:
    print("prime")"""

##exercise

import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler
from math import isnan

names = ["Age", "Age1stCode", "YearsCode", "YearsCodePro"]

df = pandas.read_csv(filepath_or_buffer="survey_results_publicCOPY.csv", usecols=names, sep=",", low_memory=False)

# for i in range(len(df["Age"])):
#     if isnan(df["Age"][i]):
#         df.drop(index=i, inplace=True)

df.dropna(subset=names, inplace=True)
# print(isnan(df["Age"][1]))
df = df[(df["YearsCodePro"] != "More than 50 years")]
df.drop()


print(df["YearsCodePro"].unique())