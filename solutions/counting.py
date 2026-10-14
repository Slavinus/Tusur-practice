def factorial(n):
    res = 1
    if n == 0:
        return(1)
    elif n < 0:
        return(None)
    else:
        for i in range(1,n+1):
            res *= i
        return res

def arrangements(n, k):
    if k > n or k < 0 or n < 0:
        return(0)
    else:
        return(factorial(n)//(factorial(n - k)))


def combinations(n, k):
    if k > n or k < 0 or n < 0:
        return(0)
    else:
        return(factorial(n)//(factorial(k)*factorial(n-k)))

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print (factorial(n))
    print (arrangements(n, k))
    print (combinations(n, k))