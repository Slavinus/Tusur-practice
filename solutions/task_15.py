def days_in_month(month, year):
    if month == 2:
        a = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if a else 28
    if month in (4, 6, 9, 11):
        return 30
    else:
        return 31

if __name__ == "__main__":
    month = int(input("Какой месяц по счёту"))
    year = int(input("Какой год"))
    print(days_in_month(month, year))