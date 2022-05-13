ary = []
x = int(input('Input Element Number: '))
for a in range(0, x):
  ele = int(input())

  ary.append(ele)

def _2v2(ary):
    for i in range(len(ary) - 1):
        if ary[i] == 2 and ary[i + 1] == 2:
            return True
    return False

_2v2(ary)