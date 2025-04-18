#Usando comprehension

squares = [x**2 for x in range(11)]
print(squares)

evens = [x for x in range(21) if x % 2 == 0]
print(evens)

celsius = [x for x in range(11)]
farenheit = [(temp * 9/5) + 32 for temp in celsius]
print(farenheit)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

tranposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(tranposed)

transpo = []

for i in range(len(matrix[0])):
    matrix_row = []
    for row in matrix:
        matrix_row.append(row[i])
    transpo.append(matrix_row)
print(transpo)