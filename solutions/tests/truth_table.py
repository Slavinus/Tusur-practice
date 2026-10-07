def truth_table(n):
    return [
        tuple(int(bit) for bit in bin(i)[2:].zfill(n))
        for i in range(2**n)
    ]

if __name__ == "__main__":
    n = int(input ())
    print (truth_table(n))