# n = int(input())
# words = [input() for i in range(n)]
# def shorter(word):
#     if len(word) <= 10:
#         return word
#     else:
#         return word[0] + str(len(word)-2) + word[-1]

# for i in words:
#     print(shorter(i))


# n = int(input())
# sol = [input().split(" ") for i in range(n)]
# soln = 0
# for item in sol:
#     if item.count("1")>=2:
#         soln += 1
# print(soln)


# n, k = input().split(" ")
# score = input().split(" ")
# count = 0
# for i in score:
#     if int(i) >= int(score[int(k) - 1]) and int(i) != 0:
#         count+=1
# print(count)


# m, n = list(map(int,input().split(" ")))
# print(m*n//2)

# from functools import reduce
# n = int(input())
# ops = [input() for i in range(n)]
# def operation_(op):
#     x = 0
#     if op.find("++") != -1:
#         x += 1
#     elif op.find("--") != -1:
#         x -= 1
#     return x
# print(sum(list(map(operation_, ops))))


# idx = [input().split() for i in range(5)]
# row = 0
# col = 0
# for id in idx:
#     row += 1
#     try:
#         col = id.index("1") + 1
#         break
#     except:
#         pass
# print(abs(3-row)+abs(3-col))


# s1 = input().lower().split(" ")
# s2 = input().lower().split(" ")
# if s1 != s2:
#     for a, b in zip(s1, s2):
#         if a == b:
#             continue
#         else:
#             if a < b:
#                 print(-1)
#             elif a > b:
#                 print(1)
# else:
#     print(0)


# s = sorted(input().split('+'))
# for num in s[:-1]:
#     print(num, end="")
#     print("+", end="")
# print(s[-1])


# A. Word Capitalization
# wprd = input()
# print(wprd[0].upper()+wprd[1:])


# A. Boy or Girl
# name = input()
# username = [i for i in name]
# username = list(set(username))
# try:
#     username.remove(" ")
# except:
#     pass
# unq = len(username)
# if unq%2 == 0:
#     print("CHAT WITH HER!")
# elif unq%2 == 1:
#     print("IGNORE HIM!")


# Stones on the Table
# n = int(input())
# s = input()
# a = 0
# for i in range(n-1):
#     if s[i] == s[i+1]:
#         a+=1
# print(a)

# Bear and Big Brother
# a, b = list(map(int, input().split(" ")))
# def time_needed(a, b):
#     t = 0
#     a1 = a
#     b1 = b
#     while a1<=b1:
#         a1 = a1*3
#         b1 = b1*2
#         t += 1
#     return t
# print(time_needed(a, b))


#Soldier and Bananas
# k, n, w = list(map(int, input().split(" ")))
# price = k*((w*(w+1))/2)
# if price<=n:
#     print(0)
# else:
#     print(int(abs(n-price)))

# Greed
# n = int(input())
# rem = list(map(int,input().split()))
# cap = sum((sorted(list(map(int,input().split()))))[-2:])
# if sum(rem)<=cap:
#     print("YES")
# else:
#     print("NO")


# Elephent
# n = int(input())
# steps = sorted([i for i in range(1,6)], reverse=True)
# step = 0
# for i in steps:
#     step += (n//i)
#     n -= (n//i)*i
# print(step)


# Word
# s = input()
# ups, lows = 0, 0
# for i in s:
#     if i.isupper():
#         ups+=1
#     elif i.islower():
#         lows += 1
# if lows>=ups:
#     print(s.lower())
# elif lows<ups:
#     print(s.upper())


# Wrong Subtraction
# n, k = list(map(int, input().split()))
# for i in range(k):
#     if n%10==0:
#         n = n/10
#     elif n%10 != 0:
#         n = n-1
# print(int(n))


# Nearly Lucky Number
# n = input()
# iv = n.count("4")
# vii = n.count("7")
# if iv+vii == 4 or iv + vii == 7:
#     print("YES")
# else:
#     print("NO")


# Encode String
# s = input()
# alpha = 'abcdefghi'
# alpha1 = [i for i in alpha]
# bets = 'jklmnopqrstuvwxyz'
# bets1 = [i for i in bets]
# encode = []
# for i in s:
#     if i in alpha:
#         encode.append(str(alpha.index(i)+1))
#     else:
#         encode.append(str(bets.index(i)+10)+'0')
# print(''.join(encode))

# Decode String
# t = int(input())
# dict = []
# for i in range(t):
#     dict.append((input(), input()))
# def decoder(data):
#     alpha = 'abcdefghi'
#     bets = 'jklmnopqrstuvwxyz'
#     data = str(data)[::-1]
#     decoded = []
#     i = 0
#     while i<len(data):
#         if data[i] != '0':
#             decoded.append(alpha[int(data[i])-1])
#             i += 1
#         else:
#             decoded.append(bets[int((data[i+2] + data[i+1]))-10])
#             i += 3
#         # print(i)
#     # print(data, decoded)
#     decoded.reverse()
#     return ''.join(decoded)
# for i in dict:
#     print(decoder(i[1]))

# n = int(input())
# s = input()
# a = s.count("A")
# d = s.count("D")
# if a>d:
#     print("Anton")
# elif d>a:
#     print("Danik")
# else:
#     print("Friendship")

# Tram
# n = int(input())
# dict = []
# for i in range(n):
#     dict.append(list(map(int,input().split())))
# min_cap = 0
# curr = 0
# for stop in dict:
#     curr += (stop[1]-stop[0])
#     if min_cap<curr:
#         min_cap += curr-min_cap
# print(min_cap)

# Queue at the School
# n, t = [int(i) for i in (input()).split()]
# q = input()
# q1 = q
# for i in range(t):
#     if q1.find('BG') == -1:
#         break
#     else:
#         q1 = q1.replace('BG', 'GB')
# print(q1)


# Below the Diagonal
# n = int(input())
# ones = []
# for i in range(n-1):
#     ones.append(list(map(int, input().split())))
# for pos in ones:


# Cut the Triangle
# def slope(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     try:
#         return (y2-y1)/(x2-x1)
#     except:
#         return "infinite"
# n = int(input())
# for i in range(n):
#     coor = []
#     a = input()
#     for i in range(3):
#         c = tuple(map(int, input().split(" ")))
#         coor.append(c)
#     p1, p2, p3 = coor
#     slopes = [slope(p1, p2), slope(p2, p3), slope(p3, p1)]
#     # prod = [slope[0]*slope[1], slope[1]*slope[2], slope[0]*slope[2]]
#     if "infinite" in slopes and 0 in slopes:
#         print("No")
#     else:
#         print("Yes")


# Block Towers
# t = int(input())
# for i in range(t):
#     n = int(input())
#     nb = [int(i) for i in input().split()]
#     # print(nb)
#     for i in range(n-1):
#         while nb[0] < (nb[i+1]):
#             # print("f2")
#             nb[0] += 1
#             nb[i+1] -= 1
#     print(nb[0])

# Vanya and Fence
# n, h = [int(i) for i in input().split()]
# w = 0
# for i in input().split():
#     a = int(i)
#     if a <= h:
#         w += 1
#     else:
#         w += 2
# print(w)

# Exchange
# t = int(input())
# for i in range(t):
#     n, a, b = [int(i) for i in input().split()]
#     if b>=a:
#         if n%a == 0:
#             print(n/a)
#         else:
#             print(n//a + 1)1
#     else:
#         print(1)

t = int(input())
for i in range(t):
    n = (input())
    ni = [int(i) for i in n]
    print(max(ni))