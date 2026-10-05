def bytes_to_kilobytes(value):
    result = value / 1024
    return result

def kilobytes_to_bytes(value):
    result = value * 1024
    return result
if __name__ == "__main__":
    bytes_to_kilobytes(2048)
    kilobytes_to_bytes(2)