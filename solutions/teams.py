def team_weights(weights):
    return (sum(weights[::2]), sum(weights[1::2]))

if __name__ == "__main__":
    a = input("Введите числа").split()
    weights = []
    for i in a:
        weights.append(int(i))
    print(team_weights(weights))