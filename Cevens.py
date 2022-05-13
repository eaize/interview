ary = []
x = int(input('Input Element Number: '))
for a in range(0, x):
  ele = int(input())

  ary.append(ele)

def evensC(ary):
  evenC = []
  oddC = []
  for v in ary:
    if v % 2 == 0:
      evenC.append(v)
    else:
      oddC.append(v)
  return len(evenC)
  return len(oddC) 