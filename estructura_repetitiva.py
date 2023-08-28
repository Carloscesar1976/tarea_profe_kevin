import random
for i in range(3):
 print(random.random())

 import random
for i in range(1):
 print(random.random())

 import random
for i in range(2):
 print(random.random())



suma=0
while True:
    numero = int(input("Ingrese un número (-1 para terminar): "))
    
    if numero == -1:
        break  
    else:
        suma += numero  

print("La sumatoria de los números ingresados es:", suma)




cantidad_numeros = int(input("Ingrese la cantidad de números : "))

mayores_cero = 0
menores_cero = 0
iguales_cero = 0

for _ in range(cantidad_numeros):
    numero = float(input("Ingrese un número: "))
    
    if numero > 0:
        mayores_cero += 1
    elif numero < 0:
        menores_cero += 1
    else:
        iguales_cero += 1

print("Cantidad de números mayores que 0:", mayores_cero)
print("Cantidad de números menores que 0:", menores_cero)
print("Cantidad de números iguales a 0:", iguales_cero)



while True:
    caracter = input("Ingrese un caracter : ")

    if caracter == '0':
        print("usted ingreso cero,fin del programa")
        break  
        
    elif caracter.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")


suma = 0
cantidad_numeros = 0


while True:
    numero = float(input("Ingrese un número: "))
    
    if numero == 0:
        print("usted ingreso cero")
        break  
    else:
        suma += numero
        cantidad_numeros += 1


if cantidad_numeros > 0:
    media = suma / cantidad_numeros
    print("Suma de los números:", suma)
    print("Media de los números:", media)
else:
    print("No se ingresaron números.")






