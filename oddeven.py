ary = []
x = int(input('Input Element Number: '))
for a in range(0, x):
  ele = int(input())

  ary.append(ele)

def numC(ary):
  evenC = []
  oddC = []
  for v in ary:
    if v % 2 == 0:
      evenC.append(v)
    elif v % 2 != 0:
      oddC.append(v)
  e = len(evenC)
  o = len(oddC)
  print ('Even numbers in the list =', e)
  print ('Odd numbers in the list =', o) 
numC(ary)