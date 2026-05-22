def toBinario(n):
    if type(n) is not int:
        return -1
    if n < 0 or n > 255:
        return -1
    return bin(n)[2:].zfill(8)

if __name__ == "__main__":
    print(toBinario(22))
    print(toBinario(129))
    print(toBinario(345))
    print(toBinario(22.5))
    print(toBinario("hola"))
    print(toBinario(-2))
