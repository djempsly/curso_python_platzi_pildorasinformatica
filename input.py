name = input('Escribe tu nombre ')
print()
age = int(input('Escribe tu edad '))

if age >= 18:
    print('Eres Mayor de edad')
    print('No tienes que esperar nada')
elif age < 18:
    my_age = (18 - age)
    print(my_age)
    print('Te falta', my_age, 'años para tener', 18, 'años')