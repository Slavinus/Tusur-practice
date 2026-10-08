def is_automorphic(n):
    return str(n**2).endswith(str(n))

if __name__ == "__main__":
    n = int(input())
    print (is_automorphic(n))