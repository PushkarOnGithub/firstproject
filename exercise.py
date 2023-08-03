import random

"""#exercise1:apni dictionary
dict={"up":"upar","down":"neeche","left":"baayen","right":"daayen"}
print("type the word to know the meaning in hindi")
word=input()
print(dict.get(word))"""

#exercise2:faulty calculator
"""n1=int(input("enter your first number:"))
o1=input("what do you want to do?")
n2=int(input("enter your second number"))
if n1==45 and o1=="*" and n2==3:
    ans=555
elif n1==56 and o1=="+" and n2==9:
    ans=77
elif n1==56 and o1=="/" and n2==6:
    ans=4
elif o1=="*":
    ans=n1*n2
elif o1=="+":
    ans=n1+n2
elif o1=="-":
    ans=n1-n2
elif o1=="/":
    ans=n1/n2
print("your answer is :",ans)"""
#exercise3:guess the number
"""attempts=10
b=attempts+1
n=random.randint(1,1000)
RunGame = True
while(RunGame):
    if(attempts==0):
        print("Game Over","The number was:",n)
        break
    elif(attempts!=0):
        print("Guess The Number Between 1 & 1000 ;You Have", attempts, "Attempt(s):")
        guess = int(input())
    if (guess < n and attempts!=0):
        print(guess,"Is Smaller Than The Number")
    elif (guess > n and attempts!=0):
        print(guess,"Is Greater Than The Number")
    else:
        print("Yes,You've Got It Right.You Won.")
        print("You Took",b-attempts,"Guesses To Guess The Number")
        break
    attempts=attempts-1
"""

#exercise4:astrologer's stars
"""l=1
m = int(input("input a number lesser than 20 to make astrologer's stars:\n"))
n = input("Choose between true and false. type 1 for true,0 for false:\n")
while m>0 and n=="0":
    print(n*("*"))
    m = m-1
while m>0 and n=="1" and l<=m:
    print(l*("*"))
    l=l+1"""

#exercise5:Health Management Sysyem
"""def getdate():
    import datetime
    return datetime.datetime.now()
g=str(getdate())

def logfile():
    user = int(input("To choose user Type 1 for Pushkar, 2 for Deepti, 3 for Bhanu:\n"))
    type = int(input("Type 1 for diet, 2 for exercise:\n"))
    return (user,type)
h=logfile()
if h == (1,1):
    data = input("enter the data:\n")
    f=open("pd.txt","a")
    f.write("{" + g + "}\t" + data +"\n")
    f.close()
elif h == (1,2):
    data = input("enter the data:\n")
    f=open("pe.txt","a")
    f.write("{" + g + "}\t" + data + "\n")
    f.close()
elif h == (2,1):
    data = input("enter the data:\n")
    f=open("dd.txt","a")
    f.write("{" + g + "}\t" + data + "\n")
    f.close()
elif h == (2,2):
    data = input("enter the data:\n")
    f=open("de.txt","a")
    f.write("{" + g + "}\t" + data + "\n")
    f.close()
elif h == (3,1):
    data = input("enter the data:\n")
    f=open("bd.txt","a")
    f.write("{" + g + "}\t" + data + "\n")
elif h == (3,2):
    data = input("enter the data:\n")
    f=open("be.txt","a")
    f.write("{" + g + "}\t" + data + "\n")
    f.close()
"""

##exercise 6 snake water gun

"""poss=["Snake", "Water", "Gun"]
import random

bot_win = 0
user_win = 0
i=1
# bot = 0
def swg(i):
    # global bot
    bot = random.choice(poss)
    print("Computer Chose", bot)
    if i == "Snake" and bot == "Snake":
        return 0
    elif i == "Snake" and bot == "Water":
        return "user"
    elif i == "Snake" and bot == "Gun":
        return "bot"
    elif i == "Water" and bot =="Water":
        return 0
    elif i == "Water" and bot =="Snake":
        return "bot"
    elif i == "Water" and bot == "Gun":
        return "user"
    elif i == "Gun" and bot == "Gun":
        return 0
    elif i == "Gun" and bot == "Water":
        return "bot"
    elif i == "Gun" and bot == "Snake":
        return "user"

while i<=10:

    user_inp = (input("Snake Water Gun\n"))[0]
    # print("Computer Chose", bot)
    Poss = {"s":"Snake", "w":"Water", "g":"Gun"}
    whowon=swg(Poss[user_inp])
    if whowon == 0:
        print("Tie This Time\n")
        continue
    else :
        if whowon == "user":

            print("You Won This Time\n")
            user_win += 1
            i += 1
        elif whowon == "bot":
            print("Computer Won This Time\n")
            bot_win+=1
            i += 1
print("You Won", user_win, "Times")
print("Computer Won", bot_win, "Times")
if user_win<bot_win:
    print("Computer Won Match")
elif user_win>bot_win:
    print("You Won The Match")
else :
    print("Overall Match Tied")
skhk = input("Game Over")"""

"""##armstrong number


def armstrong():
    #this function checks if a given number is a armstrong number


    num = input("Type your number:\n")
    temp= 0

    if not num.isnumeric():
        print("Enter a valid number")
        exit()
        # armstrong()
    else:
        for i in range(0, len(num)):
            temp += (int(num[i])) ** len(num)
            i += 1

    if int(num) == temp:
        print(num," is a Armstrong number")
    else:
        print(num," is not a Armstrong number")
armstrong()"""


##armstrong number generator


"""def armstrong(num1):
    # this function checks if a given number is a armstrong number
    num = str(num1)
    temp = 0
    for i in range(0, len(num)):
        temp += (int(num[i])) ** len(num)
        i += 1

    if int(num) == temp:
        return True
    else:
        return False

def ArmstrongNumbers():
    n = input("Input a number to generate Armstrong numbers till number: \n")
    #this function returns all Armstrong Numbers till n
    Anumbers = []
    if not str(n).isnumeric():
        print("Enter a valid number")
    else:
        for i in range(0,int(n)+1):
            if armstrong(i) == True:
                Anumbers.append(i)
                i+=1
            else:
                i+=1
                continue
    return Anumbers
print(ArmstrongNumbers())"""

# Fibonacci series
n = int(input("Enter n to find nth fibonacci number: "))
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(n))