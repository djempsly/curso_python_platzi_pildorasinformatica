datos = []

indice = 0

while indice != 5:
    dato = input(f'Escride tus datos (indice{indice}):')
    datos.append(dato)
    indice += 1

print("La familia de Miguelina tiene esos miembros ", datos)