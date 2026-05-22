def obtener_divisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def divisoresComunes(a, b):
    if type(a) is not int or type(b) is not int:
        print("No puedo calcular los divisores comunes de esos números")
        return
    if a <= 0 or b <= 0:
        print("No puedo calcular los divisores comunes de esos números")
        return
    
    div_a = obtener_divisores(a)
    div_b = obtener_divisores(b)
    
    comunes = sorted([d for d in div_a if d in div_b])
    
    if len(comunes) == 1:
        print(f"El único divisor común de {a} y {b} es: {comunes[0]}")
    else:
        comunes_str = ", ".join(map(str, comunes))
        print(f"Los divisores comunes de {a} y {b} son: {comunes_str}")

if __name__ == "__main__":
    divisoresComunes(22, 16)
    divisoresComunes(33, 17)
    divisoresComunes(1725, 2500)
    divisoresComunes(22.5, 0)
