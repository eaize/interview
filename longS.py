a = input(str())
b = input(str())

def lonShot(a, b):

  if len(a) < len(b):
    return a + b + a
  return b + a + b 
lonShot((a), (b))