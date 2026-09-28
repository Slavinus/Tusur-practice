def circle_diameter(radius):
    return radius * 2
def sum_range(start, end):
    num = 0
    for i in range(start, end+1):
        num += i
    return (num)

if __name__ == "__main__":
    radius = int(input("Введите радиус"))
    start = int(input("Введите стартовое число"))
    end = int(input("Введите конечное число"))
    print(circle_diameter(radius))
    print(sum_range(start, end))