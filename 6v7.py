ary = []
x = int(input('Input Element Number: '))
for a in range(0, x):
  ele = int(input())

  ary.append(ele)

def sum67(ary):
  t = False
  p = []
  for i in ary:
      if(i == 6):
        t = True
        continue
      if(i == 7 and t is True):
        t = False
        continue
      if(t is False):
       p.append(i)
  return sum(p)
sum67(ary)