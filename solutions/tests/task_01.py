def meters_to_centimeters(meters):
    return meters*100

if __name__ == "__main__":
    distance = float(input("Введите расстояние в метрах: "))
    print(f"Distance in centimeters: {meters_to_centimeters(distance)}")