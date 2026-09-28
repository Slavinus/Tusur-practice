def shortest_distance(kilometers, meters):
    kilometers = kilometers * 1000
    return int(min(kilometers,meters))

if __name__ == "__main__":
    kilometers = float(input("Введите километры"))
    meters = int(input("Введите метры"))
    print(shortest_distance(kilometers, meters))