def find_even_index(numbers):
    total_sum = sum(numbers)
    left_sum = 0

    for i, num in enumerate(numbers):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1

print (find_even_index([1, 2, 3, 4, 3, 2, 1]))
print (find_even_index([1, 100, 50, -51, 1, 1]))
print (find_even_index([20, 10, -80, 10, 10, 15, 35]))
print (find_even_index([1, 2, 3, 4, 5, 6]))