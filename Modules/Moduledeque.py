from collections import deque

# it is like a list. we use deque because accessing it is faster than a list

deque = deque("hello")    # creating a deque object

print(deque)

deque.extend("this is pushkar")
print(deque)

deque.extendleft("hehe")
print(deque)

deque.append(1)
print(deque)

deque.appendleft("Hii")
print(deque)

deque.pop()
print(deque)

deque.popleft()
print(deque)

deque.clear()
print(deque)

deque.rotate(-1)    # consider elements of the deque in a circle and rotate()  rotates the circle with given argument
print(deque)

deque.clear()

d = deque("hey", maxlen=5)   # deque length cannot be max than 5 now
d.append(1)
print(d)
d.append(2)
print(d)
d.append(3)
print(d)

