def bytes_to_kilobytes(value):
    return value / 1024
def kilobytes_to_bytes(value):
    return value * 1024

if __name__ == "__main__":
    value = float(input("Введите число"))
    direction = input().strip().lower()
    print (bytes_to_kilobytes(value))
    print (kilobytes_to_bytes(value))