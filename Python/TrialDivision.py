import math
def trial_division(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
          return print(False)
          #return False
    return print(True)

def trial_division_2(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    
    for i in range(2, int(math.sqrt(n))):
        if (n % i == 0):
          return print(False)
          #return False
    return print(True)


def trial_division_3(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    if (n % 2 == 0):
        return print(False)
    for i in range(3, int(math.sqrt(n)),2):
        if (n % i == 0):
          return print(False)
          #return False
    return print(True)

def trial_division_4(n):
    if (n <= 1):
        return print(False)
    if (n <= 3):
        return print(True)
    if (n % 2 == 0):
        return print(False)
    if (n % 3 == 0):
        return print(False)
    if (n % 5 == 0):
        return print(False)
    for i in range(3, int(math.sqrt(n)),2):
        if (n % i == 0):
          return print(False)
          #return False
    return print(True)


def trial_division_5(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if(not(n & 1)):
        return False
    if (n % 3 == 0):
        return False
    if (n % 5 == 0):
        return False
    for i in range(3, int(math.sqrt(n))):
        if (n % i == 0):
          return False
          #return False
    return True


    

if __name__ == "__main__":
    pass