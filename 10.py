ary = []
x = int(input('Input Element Number: '))
for a in range(0, x):
  ele = int(input())

  ary.append(ele)
for ary in range(x+1):
  for i in range(ary):
    print(ary, end=" ")
  print("")