# Variables de tasas de cambio (1 Euro como base)
EURO_A_PESO = 27.93
EURO_A_RUPIA = 102.81
EURO_A_FRANCO = 0.93

def conversor():
    try:
        # Pedir entrada al usuario
        entrada = input("Introduce la cantidad: ").strip()
        
        if not entrada:
            print("Error: No se ha introducido ninguna cantidad.")
            return

        # Manejar la coma como separador decimal
        entrada_limpia = entrada.replace(',', '.')
        
        # Extraer el valor numérico y la letra de la moneda
        # Usamos try-except para capturar errores de conversión a float
        try:
            valor_num = float(entrada_limpia[:-1])
        except ValueError:
            print("Error: La parte numérica de la entrada no es válida.")
            return
            
        moneda = entrada_limpia[-1].upper()

        # Validar que la moneda sea una de las permitidas
        if moneda not in ['E', 'P', 'R', 'F']:
            print(f"Error: La moneda '{moneda}' no es reconocida. Use E, P, R o F.")
            return

        if moneda == 'E':
            p = valor_num * EURO_A_PESO
            r = valor_num * EURO_A_RUPIA
            f = valor_num * EURO_A_FRANCO
            print(f"{valor_num} euros equivalen a {p:.4f} pesos cubanos, {r:.4f} rupias o {f:.4f} francos suizos")
        
        elif moneda == 'P':
            e = valor_num / EURO_A_PESO
            print(f"{valor_num} pesos cubanos equivalen a {e:.4f} euros")
            
        elif moneda == 'R':
            e = valor_num / EURO_A_RUPIA
            print(f"{valor_num} rupias equivalen a {e:.4f} euros")
            
        elif moneda == 'F':
            e = valor_num / EURO_A_FRANCO
            print(f"{valor_num} francos suizos equivalen a {e:.4f} euros")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    conversor()