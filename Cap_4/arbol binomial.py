import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def generar_arbol(n, valores):
    if n == 0:
        return None
    valor = random.randint(1, 20)
    while valor in valores:
        valor = random.randint(1, 20)
    raiz = Nodo(valor)
    valores.add(valor)
    raiz.izquierda = generar_arbol(n//2, valores)
    raiz.derecha = generar_arbol(n//2, valores)
    return raiz

def preorden(raiz):
    if raiz is None:
        return []
    return [raiz.valor] + preorden(raiz.izquierda) + preorden(raiz.derecha)

def inorden(raiz):
    if raiz is None:
        return []
    return inorden(raiz.izquierda) + [raiz.valor] + inorden(raiz.derecha)

def postorden(raiz):
    if raiz is None:
        return []
    return postorden(raiz.izquierda) + postorden(raiz.derecha) + [raiz.valor]

# Generar un árbol binario aleatorio con 10 nodos
valores = set()
arbol = generar_arbol(10, valores)

# Ordenar el árbol por preorden, inorden y postorden
pre = preorden(arbol)
inor = inorden(arbol)
post = postorden(arbol)

# Imprimir los resultados
print("Árbol binario aleatorio:")
print("           " + str(arbol.valor))
print("          / \\")
print("        " + str(arbol.izquierda.valor) + "   " + str(arbol.derecha.valor))
print("       / \\   / \\")
print("      " + str(arbol.izquierda.izquierda.valor) + "   " + str(arbol.izquierda.derecha.valor) + " " + str(arbol.derecha.izquierda.valor) + "   " + str(arbol.derecha.derecha.valor))
print("Preorden:  " + str(pre))
print("Inorden:   " + str(inor))
print("Postorden: " + str(post))
