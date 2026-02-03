#1
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#2
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) #False 

#3
x = 5

print(x > 0 and x < 10)

#4
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#5
x = 5

print(not(x > 3 and x < 10))
