def echo_number(number):
    return f"Thats the number you entered {number}"

if __name__ == "__main__":
    number = input("Введите число")
    print(echo_number(number))