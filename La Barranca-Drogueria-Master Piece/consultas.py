#Devuelve lista con las ultimas ventas
def ultimas_ventas(registros, cantidadregistro):
    ultimasventas = []
    ultimosreg = registros.reverse()
    while cantidadregistro > len(registros):
        cantidadregistro = cantidadregistro - 1
    for i in range(cantidadregistro):
        ultimasventas.append(registros[i])
    return ultimasventas



#Devuelve el cliente a buscar
def buscar_cliente(registros, nombre):
    cliente = []
    for i in range(len(registros)):
        if nombre in registros[i].cliente:
            if registros[i].cliente in cliente:
                pass
            else:
                cliente.append(registros[i].cliente)
        else:
            pass
    return cliente
# Devuelve en una lista todos los productos que compro el cliente
def productos_cliente(registros, cliente):
    nombre_cliente = cliente.upper()
    productos = []
    for i in range(len(registros)):
        if nombre_cliente in registros[i].cliente:
            productos.append(registros[i])
    return productos



# Devuelve una lista con los productos que coincidan con los al menos 3 caracteres ingresados

def buscar_productos(registros, nombre):
    producto = []
    for i in range(len(registros)):
        if nombre in registros[i].producto:
            if registros[i].producto in producto:
                pass
            else:
                producto.append(registros[i].producto)
        else:
            pass
    return producto
# Devuelve en una lista el producto y lo clientes que lo compraron
def lista_producto(registros, producto):
    nombre_producto = producto.upper()
    cliente = []
    for i in range(len(registros)):
        if nombre_producto in registros[i].producto:
            cliente.append(registros[i])
    return cliente

# 
# Devuelve lista los productos que mas se vendieron Ordenados de mayor a menor

def masvendidos(registros, cantidad):
    producto = []
    cantidad_produc = []
    colunna = 0
    for i in range(len(registros)):
        if i == 0:
            producto.append(registros[i].producto)
            cantidad_produc.append([])
            cantidad_produc[colunna] = [0, registros[i]]
        else:
            if registros[i].producto in producto:
                pass
            else:
                colunna = colunna + 1
                producto.append(registros[i].producto)
                cantidad_produc.append([])
                cantidad_produc[colunna] = [0, registros[i]]
    for i in range(len(producto)):
        for x in range(len(registros)):
            if producto[i] in registros[x].producto:
                cantidad_produc[i][0] = cantidad_produc[i][0] + registros[x].cantidad
            else:
                pass
    cantidad_produc.sort(reverse = True)
    while cantidad > len(producto):
        cantidad = cantidad - 1
    lista_producto = []
    for i in range(cantidad):
        lista_producto.append([0] * 2)
        lista_producto[i][0] = cantidad_produc[i][0]
        lista_producto[i][1] = cantidad_produc[i][1]
    return lista_producto



# Devuelve lista de los clientes que mas gastaron y los ordena de mayor a menor

def clientes_masgastaron(registros, cantidad):
    clientes = []
    cantidadclientes = []
    colunna = 0
    for i in range(len(registros)):
        if i == 0:
            clientes.append(registros[i].cliente)
            cantidadclientes.append([])
            cantidadclientes[colunna] = [0, registros[i]]
        else:
            if registros[i].cliente in clientes:
                pass
            else:
                clientes.append(registros[i].cliente)
                colunna = colunna + 1
                cantidadclientes.append([])
                cantidadclientes[colunna] = [0, registros[i]]
    for i in range(len(clientes)):
        for x in range(len(registros)):
            if clientes[i] in registros[x].cliente:
                cantidadclientes[i][0] = cantidadclientes[i][0] + (registros[x].cantidad * registros[x].precio)
            else:
                pass
    cantidadclientes.sort(reverse = True)
    while cantidad > len(clientes):
        cantidad = cantidad - 1
    lista_clientes = []
    for i in range(cantidad):
        lista_clientes.append([0] * 2)
        lista_clientes[i][0] = cantidadclientes[i][0]
        lista_clientes[i][1] = cantidadclientes[i][1]
    return lista_clientes
