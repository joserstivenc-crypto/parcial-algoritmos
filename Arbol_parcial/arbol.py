
import matplotlib.pyplot as plt
import networkx as nx

# CREAR EL ARBOL
arbol = nx.DiGraph()

aristas = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6), (3, 7),
    (4, 8),
    (5, 9), (5, 10),
    (6, 11),
    (7, 12)
]

arbol.add_edges_from(aristas)

# POSICIONES
posiciones = {
    1: (0, 3),
    2: (-1, 2), 3: (1, 2),
    4: (-1.5, 1), 5: (-0.5, 1),
    6: (0.5, 1), 7: (1.5, 1),
    8: (-1.5, 0),
    9: (-0.75, 0),
    10: (-0.25, 0),
    11: (0.5, 0),
    12: (1.5, 0)
}

# DIBUJAR
plt.figure(figsize=(10, 6))


# NOMBRES DE LOS CARGOS
nombres = {
    1: "Gerente\nGeneral",
    2: "Gerente\nAdministrativo",
    3: "Gerente\nComercial",
    4: "Supervisor\nRRHH",
    5: "Supervisor\nFinanciero",
    6: "Supervisor\nVentas",
    7: "Supervisor\nAtencion",
    8: "Empleado\nRRHH",
    9: "Auxiliar\nFinanciero",
    10: "Contador",
    11: "Asesor\nVentas",
    12: "Asesor\nAtencion"
}

plt.figure(figsize=(15, 9))

nx.draw(
    arbol,
    posiciones,
    labels=nombres,
    with_labels=True,
    node_size=3000,
    node_color="lightgreen",
    font_size=8,
    font_weight="bold",
    arrows=True,
    arrowsize=15,
    edge_color="gray"
)

plt.title("Estructura organizacional de una empresa")
plt.axis("off")

plt.savefig("empresa_arbol.png", dpi=300, bbox_inches="tight")
plt.show()

# RECORRIDO PREORDEN
def preorden(nodo):
    resultado = [nodo]
    for hijo in arbol.successors(nodo):
        resultado.extend(preorden(hijo))
    return resultado

# RECORRIDO INORDEN
def inorden(nodo):
    hijos = list(arbol.successors(nodo))

    if len(hijos) == 0:
        return [nodo]

    if len(hijos) == 1:
        return inorden(hijos[0]) + [nodo]

    return inorden(hijos[0]) + [nodo] + inorden(hijos[1])

# RECORRIDO POSTORDEN
def postorden(nodo):
    resultado = []

    for hijo in arbol.successors(nodo):
        resultado.extend(postorden(hijo))

    resultado.append(nodo)
    return resultado



# IDENTIFICACION DE LOS NODOS

raiz = 1

# Nodos del arbol
nodos = list(arbol.nodes())

# Nodos hoja (sin hijos)
hojas = [
    nodo for nodo in arbol.nodes()
    if arbol.out_degree(nodo) == 0
]

# Nodos internos (con hijos)
internos = [
    nodo for nodo in arbol.nodes()
    if arbol.out_degree(nodo) > 0
]

# Cantidad de nodos y conexiones
cantidad_nodos = arbol.number_of_nodes()
cantidad_aristas = arbol.number_of_edges()

# Mostrar informacion
print("\n===== INFORMACION DEL ARBOL =====")
print("Raiz:", raiz)
print("Todos los nodos:", nodos)
print("Nodos hoja:", hojas)
print("Nodos internos:", internos)
print("Cantidad de nodos:", cantidad_nodos)
print("Cantidad de aristas:", cantidad_aristas)

# MOSTRAR RESULTADOS
print("\n===== RECORRIDOS DEL ARBOL =====")

print("PREORDEN:", preorden(1))
print("INORDEN:", inorden(1))
print("POSTORDEN:", postorden(1))

# MOSTRAR IMAGEN
plt.show()


# GUARDAR RESULTADOS EN UN ARCHIVO TXT

with open("resultados_parcial.txt", "w", encoding="utf-8") as archivo:

    archivo.write("PARCIAL FINAL - ESTRUCTURAS DE DATOS\n")
    archivo.write("ARBOL BINARIO\n\n")

    archivo.write("Raiz: 1\n")
    archivo.write(f"Cantidad de nodos: {cantidad_nodos}\n")
    archivo.write(f"Cantidad de aristas: {cantidad_aristas}\n")

    archivo.write(f"Nodos hoja: {hojas}\n")
    archivo.write(f"Nodos internos: {internos}\n\n")

    archivo.write("RECORRIDOS DEL ARBOL\n")
    archivo.write(f"Preorden: {preorden(1)}\n")
    archivo.write(f"Inorden: {inorden(1)}\n")
    archivo.write(f"Postorden: {postorden(1)}\n")

print("\nArchivo de resultados guardado correctamente.")

