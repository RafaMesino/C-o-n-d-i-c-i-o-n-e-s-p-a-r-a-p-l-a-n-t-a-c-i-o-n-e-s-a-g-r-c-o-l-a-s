def obtener_datos():
    lecturas = []
    n = int(input("Ingrese el número de lecturas a realizar: "))
    
    for i in range(n):
        print(f"\nLectura #{i + 1}")
        altura = float(input("Ingrese la altura sobre el nivel del mar (msnm): "))
        profundidad = float(input("Ingrese la profundidad efectiva del suelo (cm): "))
        lecturas.append({"altura": altura, "profundidad": profundidad})
    
    return lecturas

def clasificar_altura(altura):
    if 400 <= altura <= 800:
        return "sumamente apto"
    elif altura < 400 or 801 <= altura <= 999:
        return "moderadamente apto"
    elif 1000 <= altura <= 1200:
        return "marginalmente apto"
    else:
        return "no apto"

def clasificar_profundidad(profundidad):
    if profundidad > 100:
        return "sumamente apto"
    elif 50 <= profundidad <= 100:
        return "moderadamente apto"
    elif 25 <= profundidad < 50:
        return "marginalmente apto"
    else:
        return "no apto"

# Orden para comparar categorías
orden = {
    "sumamente apto": 1,
    "moderadamente apto": 2,
    "marginalmente apto": 3,
    "no apto": 4
}

def determinar_categoria_final(cat_altura, cat_profundidad):
    if cat_altura == cat_profundidad:
        return cat_altura
    else:
        return cat_altura if orden[cat_altura] > orden[cat_profundidad] else cat_profundidad

def analizar_lecturas(lecturas):
    suma_altura = 0
    suma_profundidad = 0
    conteo_categorias = {
        "sumamente apto": 0,
        "moderadamente apto": 0,
        "marginalmente apto": 0,
        "no apto": 0
    }

    for lectura in lecturas:
        altura = lectura["altura"]
        profundidad = lectura["profundidad"]

        cat_altura = clasificar_altura(altura)
        cat_profundidad = clasificar_profundidad(profundidad)
        categoria_final = determinar_categoria_final(cat_altura, cat_profundidad)

        lectura["categoria_final"] = categoria_final

        suma_altura += altura
        suma_profundidad += profundidad
        conteo_categorias[categoria_final] += 1

    promedio_altura = round(suma_altura / len(lecturas), 2)
    promedio_profundidad = round(suma_profundidad / len(lecturas), 2)

    return promedio_altura, promedio_profundidad, conteo_categorias, lecturas

def mostrar_resultados(promedio_altura, promedio_profundidad, conteo_categorias, lecturas):
    print(f"\nPromedio de altura: {promedio_altura}")
    print(f"Promedio de profundidad: {promedio_profundidad}\n")

    for categoria, cantidad in conteo_categorias.items():
        print(f"{categoria}: {cantidad}")

    print("\nResultados por lectura:")
    for i, lectura in enumerate(lecturas):
        print(f"Lectura #{i+1} -> Categoría final: {lectura['categoria_final']}")

# Función principal
def main():
    lecturas = obtener_datos()
    promedio_altura, promedio_profundidad, conteo_categorias, lecturas = analizar_lecturas(lecturas)
    mostrar_resultados(promedio_altura, promedio_profundidad, conteo_categorias, lecturas)

# Ejecutar el programa
if __name__ == "__main__":
    main()
