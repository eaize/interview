n = False

x = int(input())
if x > 1:
  for x in range(2, x):
    if (x % 1) == 0:
      n = True
      break
if n:
  print("Not Prime")
else:
  print("Prime")