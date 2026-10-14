def compare(m, n):
    if m > n:
        return 'Number m > n'
    elif m < n:
        return 'Number m < n'
    else:
        return 'The numbers are equal'

if __name__ == "__main__":
    m = int(input("Введите m"))
    n = int(input("Введите n"))
    print(compare(m, n))