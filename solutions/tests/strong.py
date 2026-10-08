import math
def is_strong(n):
    sumF = sum(math.factorial(int(a)) for a in str(n))
    return sumF == n

if __name__ == "__main__":
    n = int(input())
    print(is_strong(n))