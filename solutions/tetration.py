def tetration(x, n):
    if n == 0:
        return 1
    return x ** tetration(x, n - 1)

if __name__ == "__main__":
    n = int(input())
    x = int(input())
    print(tetration(x, n))