from modules.nuevoarbol import ArbolBinario

# Insertar casos LL (30, 20, 10) debería provocar una rotación simple a derecha
arbolillo = ArbolBinario()
for valor in [30, 20, 10]:
    arbolillo.agregar(valor, valor)

print("Recorrido inorden:")
arbolillo.print_inorder()  # Debería imprimir: 10, 20, 30

# Verificar que el árbol esté balanceado
assert arbolillo.check_balance(), "El árbol no está balanceado."

# Verificar cuál es la raíz actual
raiz = arbolillo.raiz
print(f"La raíz actual es: {raiz.clave}")
assert raiz.clave == 20, "La raíz debería ser 20 después de balancear (caso LL)"
