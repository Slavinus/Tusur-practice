def truth_table(n):
    result = []
    if n == 0:  result.append(())
    else:
        for i in range(2**n): result.append(tuple(map(int,bin(i)[2:].zfill(n))))
    return result

def de_morgan_left(a, b):
    return not (a and b)

def de_morgan_right(a, b):
    return (not a) or (not b)

def wrong(a, b):
    return (not a) and (not b)



def are_equivalent(f, g, n):
    for row in truth_table(n):
        if f(*row) != g(*row):
            return False
    return True