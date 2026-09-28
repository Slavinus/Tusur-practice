def multiplication_table(n):
    for i in range(1,11):
        return (f"{n} * {i} = {n*i}")

if __name__ == "__main__":
    n = int(input("Введите число n"))
    print(multiplication_table(n))