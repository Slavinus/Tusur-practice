def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == "__main__":
    a = int(input("a"))
    b = int(input("b"))
    print(swap(a, b))
