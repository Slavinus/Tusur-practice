def index_of_min(values):
    if not values:
        return -1
    return values.index(min(values))

if __name__ == "__main__":
    parts = input("Введите числа").split()
    values = []
    for p in parts:
        values.append(int(p))
    print(index_of_min(values))