def greet(username):
    return f"Hello, {username}"

if __name__ == "__main__":
    username = input("Введите ваше имя")
    print(greet(username))