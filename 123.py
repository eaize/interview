ary = []
x = int(input('Input Element Number: '))
for a in range(0, x):
  ele = int(input())

  ary.append(ele)

def ary1t3(ary):
  c = 0
  f = False
  while c <= (len(ary) - 2):
    if ary[c] == 1 and ary[c+1] == 2 and ary[c+2] == 3:
      f = True
    c += 1
  return f

ary1t3(ary)