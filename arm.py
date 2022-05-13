x = int(input("Enter a number: "))
c = 0

v = x
while v > 0:
   b = v % 10
   c += b ** 3
   v //= 10

if x == c:
   print("Armstrong number")
else:
   print("Not Armstrong number")