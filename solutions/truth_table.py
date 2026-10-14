def truth_table(n):
    result = []
    if n == 0:  result.append(())
    else:
        for i in range(2**n): result.append(tuple(map(int,bin(i)[2:].zfill(n))))
    return(result)
