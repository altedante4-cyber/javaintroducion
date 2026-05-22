def toDecimal(binario):
    for c in binario:
        if c not in ('0', '1'):
            return -1
    return int(binario, 2)

if __name__ == "__main__":
    print(toDecimal("10110"))
    print(toDecimal("345"))
    print(toDecimal("hola"))
