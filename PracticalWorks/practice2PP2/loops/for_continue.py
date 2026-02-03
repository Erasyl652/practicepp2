#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#2
for n in [1,0,2,3]:
    if n == 0: continue
    print(n)


#3
for i in range(6):
    if i % 2 == 0: continue
    print(i)


#4
numbers = [4, -1, 7, -3, 2]
total = 0
for n in numbers:
    if n < 0: continue
    total += n
print(total)


#5
words = ["apple","skip","banana","cat","grape"]
for w in words:
    if len(w) <= 4 or w == "skip": continue
    print(w)
