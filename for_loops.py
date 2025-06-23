print("range 10")
for i in range (10):
    if i == 7:
        break
    if i == 5:
        continue
    print(i)

print ("Even 2 to 20")
for r in range (2,22,2):
    print(r)


print("1 to 100 sum")
total = 0
for i in range(1,101):
    print(f"Number {i}")
    total = total + i
    print(f"the total is {total}")




