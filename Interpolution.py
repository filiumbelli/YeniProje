x1=int(input("First Val: "))
x2=int(input("Second Val: "))
x3=int(input("Desired Val: "))

y1=float(input("First Val Reference: "))
y2=float(input("Second Val Reference: "))


y3 = (((y1-y2) * (x3-x2)) / (x1-x2)) + y2

print(y3)