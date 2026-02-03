#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#2
for i in range(5):
    if i == 3: break
    print(i)


#3
total = 0
for i in range(1,10):
    total += i
    if total > 10: break
    print(total)


#4
for n in [1,2,-1,3]:
    if n < 0: break
    print(n)


#5
for c in "abcdef":
    if c == "c": break
    print(c)
