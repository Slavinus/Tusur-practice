def multiplication_table(n):
    res = []
    for i in range(1,11):
        res.append(f"{n} x {i} = {n*i}")
    return res
if __name__ == "__main__":
    multiplication_table(7)