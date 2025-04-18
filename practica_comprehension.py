# para buscar los numeros cuadrado

square = [x**2 for x in range(1,10)]
print(square)

# Ahora voy a ver si puedo convertir de celsius a farenheit

celsius = [temp for temp in range (1,10)]
farenheit = [(temp * 9/5) + 32 for temp in celsius]
print(farenheit)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

tranposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(tranposed)

tranposed = []

for i in range(len(matrix[0])):
    tranposed_row = []
    for row in matrix:
        tranposed_row.append(row[i])
    tranposed.append(tranposed_row)

print(tranposed)

evens = [x for x in range(1, 21) if x%2==0]
print(evens)

events=[]

for x in range(1, 21):
    if x%2==0:
        events.append(x)
print(events)
        