from string import ascii_lowercase
from string import ascii_letters
from string import digits
from string import punctuation
from random import randint
from random import choice

def generate(len):
    clave = ''
    for i in range(int(len)):
        clave += choice(ascii_lowercase)
    return clave
def add_mayus(len):
    clave = ''
    for i in range(int(len)):
        clave += choice(ascii_letters)
    return clave
def add_num(clave, len):
    auxiliar = list(clave)
    for i in range(int(len)):
        auxiliar.pop(randint(0,int(len)-1))
        auxiliar.insert(randint(0,int(len)),choice(digits))
    clave = ''.join(auxiliar)
    print(clave)
    return clave
def add_sym(clave, len):
    auxiliar = list(clave)
    for i in range(int(len)):
        auxiliar.pop(randint(0,int(len)-1))
        auxiliar.insert(randint(0,int(len)),choice(punctuation))
    clave = ''.join(auxiliar)
    print(clave)
    return clave

print('Hola! Bienvenido a tu generador de contrasenas Por favor, dinos los parametros de la clave que deseas.')
# Longitud
len = ''
while not len.isnumeric() or int(len) < 8 or int(len) > 16:
    len = input('Longitud de la contrasena (8-16):\n')
# Con o sin etras mayusculas
lett = ''
while lett != 'Y' and lett != 'N':
    lett = input('Contiene letras mayusculas? (Y/N):\n').upper()
# Con o sin numeros
num = ''
while num != 'Y' and num != 'N':
    num = input('Contiene numeros? (Y/N):\n').upper()
# Con o sin simbolos
sym = ''
while sym != 'Y' and sym != 'N':
    sym = input('Contiene simbolos? (Y/N):\n').upper()

password = generate(len)
if lett == 'Y':
    password = add_mayus(len)
if num == 'Y':
    password = add_num(password, len)
if sym == 'Y':
    password = add_sym(password, len)

print(password)