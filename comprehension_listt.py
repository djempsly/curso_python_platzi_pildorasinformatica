# Las comprehensions list se usan para poder obtener listas de manera mas faácil. Primero se debe poner la fórmula y luego lo que queremos hacer

square = [x**2 for x in range(1,11)]
# print(square)

triangle = [y**3 for y in range(3,9)]
print(triangle)

range1 = int(input('Escribe el primer rango'))
range2= int(input('Escribe el segundo rango'))
celcius = [x for x  in range(range1, range2)]
farenheit = [(temp * 9/5) + 32 for temp in (celcius)]
print(farenheit)

evens = [y for y in range(1, 21) if y%2 == 0 ]
print(evens)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0])) ]
print(transposed)

# ahora voy a hacer el mismo transpuesto linea de codigo por linea de codigo

transpose = []

for i in range(len(matrix[0])):
    tranposed_row = []
    for row in matrix:
        tranposed_row.append(row[i])
    transpose.append(tranposed_row)
print(transpose)

