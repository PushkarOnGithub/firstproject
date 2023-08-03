""""#quiz1:adder
print("To add your numbers write them when prompted")
print("what is your first number")
num1=input()
print("what is your second number")
num2=input()
print("your sum is",int(num1)+int(num2))"""

#quiz 2:driving licence
"""print("what is your age?")
userage=int(input())
logicalage=["chutiya samjha h kya?😎😎",userage]
if 6<=userage<=80:
    logicalage.append(userage)
else :
    print(logicalage[0])
if logicalage[1]<18:
    print("you are under 18,you cannot drive")
elif logicalage[1]==18:
    print("you are 18,we are not certain wheather you can drive or not,we have to physically check the parameters")
else :
    print("you are 18+ ,you can drive")"""

#quiz3:print number from a list only if the number is greater than 6
list1=["east",344,"west",455,"north",677,"south",788]
for item in list1:
    if str(item).isnumeric() and item<500:
        print(item)

#quiz4
"""while(True):
    num = int(input("enter your number:"))
    if num<=1000:
        continue
    print("congratulations you've got number greater than 1000,",num)"""