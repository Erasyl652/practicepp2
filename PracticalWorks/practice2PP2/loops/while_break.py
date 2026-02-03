#1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#2
while True:
    text = input("Type something (or 'stop' to quit): ")
    if text == "stop":
        break
    print("You typed:", text)

#3
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total:", total)

#4
i = 0
while True:
    i += 1
    if input() == "yes" or i==3: break

#5
while True:
    if input() == "stop": break