def century_message(name, age, current_year):
    b = current_year + (100 - age)
    return f"{name}, тебе исполнится 100 лет в {b} году"

if __name__ == "__main__":
    name = input("Введите имя")
    age = int(input("Введите возраст"))
    from datetime import date
    current_year = date.today().year
    print(century_message(name, age, current_year))