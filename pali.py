while True:
    try:
      x = str(int(input()))
      n = str(int(x [::-1]))
      if x == n:
        print ("Palindrome")
      else:
        print ("Not Palindrome")
    except ValueError as e:
            print("Not an integer.")
    break