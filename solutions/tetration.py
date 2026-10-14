def tetration(x, n):
    a = 1
    for i in range(x):
        a = n ** a
    return a

if __name__ == "__main__":
    n = int(input())
    x = int(input())
    print(tetration(x, n))