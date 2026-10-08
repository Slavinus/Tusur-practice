def is_tidy(n):
    a = str(n)
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    print(is_tidy(n))