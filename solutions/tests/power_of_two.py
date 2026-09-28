def is_power_of_two(n):
    if int.bit_count(n) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("Введите число"))
    print(is_power_of_two(n))