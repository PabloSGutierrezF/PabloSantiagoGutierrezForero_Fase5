#=======================================================================================================
# Nombre del Estudiante: Pablo Santiago Gutierrez Forero
# Grupo: 213022_1097
# Programa: Ingenieria Multimedia
# Codigo fuente: Autoridad propia
# Probela 3: Matriz de información de inventario
#=======================================================================================================

print("==================================================================================================")
print("Nombre del Estudiante: Pablo Santiago Gutierrez Forero")
print("Grupo: 213022_1097")
print("Programa: Ingenieria Multimedia")
print("Codigo fuente: Autoridad propia")
print("Probela 3: Matriz de información de inventario")
print("==================================================================================================")

def calcular_cantidad_a_pedir(stock_actual: int, stock_minimo: int) -> int:
    """Determina la cantidad exacta a pedir para un articulo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

def generar_reporte_reabastecimiento (inventario: list[list]) -> None:
    """Muestra el nombre de cada articulo y la cantidad exacta a solicitar."""
    print("Reporte de reabastecimiento:")
    for articulo in inventario:
        _, nombre, stock_actual, stock_minimo = articulo
        cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"-{nombre}: {cantidad_a_pedir} unidades")

# Matriz con al menos 5 articulos:
# [Codigo del articulo, Nombre del articulo, Stock actual, Stock minimo requerido]
matriz_inventario = [
    ["A001", "Tableta Grafica", 4, 10],
    ["A002", "Lapiz optico", 25, 15],
    ["A003", "Monitor 27 pulgadas", 6, 6],
    ["A004", "Cable USB-C", 8, 20],
    ["A005", "Teclado mecanico", 12, 10],
    ["A006", "Mouse inalambrico", 3, 9],
]

if __name__ == "__main__":
    generar_reporte_reabastecimiento(matriz_inventario)
