def guests_by_seat(seats):
    result = [0] * len(seats)
    for guest, seat in enumerate(seats, start=1):
        result[seat - 1] = guest
    return result

if __name__ == "__main__":
    sit = input("Введите числа").split()
    num = []
    for i in sit:
        num.append(int(i))
    print (guests_by_seat(num))