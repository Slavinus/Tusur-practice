def to_jaden_case(text):
    return " ".join(word.capitalize() for word in text.split(" "))

if __name__ == "__main__":
    text = input("Введите ваш текст")
    print(to_jaden_case(text))