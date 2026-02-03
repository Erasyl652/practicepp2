#1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#2
while True:
    x = input()
    if x == "": continue
    print(x)

#3
n = 0
while n < 10:
    n += 1
    if n % 2 != 0: continue
    print(n)


#4
while True:
    a = input()
    if a != "yes": continue
    print("Thanks!")
    break


#5
n=0
while n<10:
    n+=1
    if n%3:continue
    print(n)
