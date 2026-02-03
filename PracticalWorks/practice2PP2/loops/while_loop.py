#1
x = 0

while x < 9:
  print(x)
  x += 1

#2
while True: #Infinite loop
  print('x')

#3
num = int(input())
while num != 5:
  print('Wrong')
print('You guessed the number')

#4
fruits =['apple','banana','orange','pineapple']
i = 0
while i < len(fruits):
  print(cities[i])
  i += 1

#5
total = 0
number = -1

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number

print("The total sum is:", total)
