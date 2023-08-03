import random

hw = []
lk = []
dict = {}
for i in range(20000):
    hw1 = random.randint(1,100)
    lk1 = random.randint(0,100)
    hw.append(hw1)
    lk.append(lk1)
    dict[hw1] = lk1
hw_ = hw.copy()
lk_ = lk.copy()
# hw_.sort()
# lk_.sort()

# print(hw.count(100))
# print(hw_.count(98))

# print(dict)
# print(list(dict))
# print(list(dict)[1])
chance = {}

print(dict[list(dict)[0]])
for i in range(100):
    chance[dict[list(dict)[i]]] = 0.95*(list(dict)[i]) + 0.05*(dict[list(dict)[i]])

