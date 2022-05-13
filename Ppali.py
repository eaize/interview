import math;

t = False
while t == False:
    try:
      x = str(int(input()))
      n = str(int(x [::-1]))
      b = int(x)
      d = int(n)
      if x == n:
        i = 1
      else:
        i = 0

      r = int(math.sqrt(b))
      v = str(r)
      g = int(math.pow(r, 2))
      z = str(g)
      if v == v[::-1]:
        j = 1
      else:
        j = 0
      if z == z[::-1]:
        w = 1
      else:
        w = 0
      if i + j + w == 3:
        h = 1
      else:
        h = 0
      if h == 1:
        print("is A Perfect Palindrome")
      else:
        print("is Not a Perfect Palindrome")
    except ValueError as e:
      t = True
      if t == True:
        print("Not an integer.")
    break