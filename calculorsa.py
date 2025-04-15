# calculando clave RSA

a= 4391 
q = 6659 


c= a * q 

print(c)

e = c - a - q + 1

print(e)


# es clave diff

p= 29
g=3

# ALicia eslige a
a= 13

#Bob elige b
b=15

ali = 3**13 %29

print(ali)

bob = 3**b %p

print(bob)

# CLave publica descubriendo los secretos

se_bob = bob**a % p
se_ali = ali**b % p

print( se_bob, se_ali)


print()
print()

A = 5**12 %29
print(A)

B= 5**17 %29

print(B)

kno = 9**12 %29
print(kno)