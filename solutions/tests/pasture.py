def pasture_area(wire, w):
    l = (wire - 2*w) / 3
    return l*w

def best_pasture(wire):
    a = -2/3
    b = wire / 3
    w = -b / (2*a)
    l = (wire - 2*w) / 3
    return w, l, pasture_area(wire, w)

if __name__ == "__main__":
    wire = int(input ())
    w = int(input ())
    print (pasture_area(wire, w))
    print(best_pasture(wire))