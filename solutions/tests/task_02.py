def bytes_to_kilobytes(value):
    return value / 1024
def kilobytes_to_bytes(value):
    return value * 1024

if __name__ == "__main__":
    fun = int(input("Выберите функцию: Байты в килобайты - 1 или Килобайты в байты - 2"))
    value = int(input("Введите число"))
    if fun == 1:
        print(bytes_to_kilobytes(value))
    if fun == 2:
        print(kilobytes_to_bytes(value))