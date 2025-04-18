# en esta tarea voy a practicar la comprehension list

squares = [x**2 for x in range(11)]
print(squares)

for x in range(11):
    x**2
print(squares)

# Convirtiendo la temperatura en Farenheit

celcius = [x for x in range(15)]
farenheit = [(temp * 9/5) + 32 for temp in celcius]

print(farenheit)

farenheit2 = []
for temp in celcius:
    farenheit1= temp * 9/5 + 32
    farenheit2.append(farenheit1)
print(farenheit2)

evens = [x for x in range(25) if x%2==0]
print(evens)

evens2 = []
for x in range(25):
    if x % 2 == 0:
        evens2.append(x)
print(evens2)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
print(matrix)

tranpos = []

for i in range(len(matrix[0])):
    trans = []
    for row in matrix:
        trans.append(row[i])
    tranpos.append(trans)
print(tranpos)