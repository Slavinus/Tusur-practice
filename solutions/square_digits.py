def square_digits(n):
    return int("".join(str(int(digit)**2) for digit in str(n)))

if __name__ == "__main__":
    n = int(input("ВВедите число n"))
    print(square_digits(n))