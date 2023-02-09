num = ''
while not num.isnumeric():
    num = input('Ingresa un numero:\n')
a = (5*(int(num)**2)+4)  #Formula para Fibonacci
a1 = (a**(1/2))     #Raiz del numero
a2 = (a/int(a1))    #Division entre la raiz del numero
v1 = a1 == a2       #Comparacion entre los valores

b = (5*(int(num)**2)-4)  #Formula para Fibonacci
b1 = (b**(1/2))     #Raiz del numero
b2 = (b/int(b1))    #Division entre la raiz del numero
v2 = b1 == b2       #Comparacion entre los valores

if v1 != v2:
    print(f'El numero {num} pertenece a la serie Fibonacci.')
else:
    print(f'El numero {num} no pertenece a la serie Fibonacci.')