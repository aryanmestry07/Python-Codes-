aa = int(input("Enter the number of elements : "))

i = 0
bb = []
cc = []
while i < aa:
    a = int(input("Enter Element : "))
    bb.append(a)
    i += 1

print(bb)
print("The square of the numbers are:")

for x in bb:
    x = x * x
    cc.append(x)

print(cc)
