def is_divisor(a, b):
    if a == 0:
        return False
    elif b % a == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("число a"))
    b = int(input("число b"))
    print (is_divisor(a, b))