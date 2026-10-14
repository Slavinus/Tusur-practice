def month_calendar(start_weekday, days):
    first_week = ["  "] * start_weekday
    for day in range (1, 8 - start_weekday):
        first_week.append(f"{day:2}")
    lines = [" ".join(first_week)]
    current_day = 8 - start_weekday
    while current_day <= days:
        week = []
        for d in range(current_day, min(current_day + 7, days + 1)):
            week.append(f"{d:2}")
        lines.append(" ".join(week))
        current_day += 7
    return "\n".join(lines)

if __name__ == "__main__":
    start_weekday = int(input("День недели 1-го числа"))
    days = int(input("Количество дней в месяце"))
    print (month_calendar(start_weekday, days))