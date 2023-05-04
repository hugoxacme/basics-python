#Iteradores
#Sumar del 0 al 20
for numero in range(0, 20, 2):
    print(numero + 2)

for numero in range(5):
    print(numero + 1)

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
    



#while

numero = 50
contador = 0

while contador < numero:
    print(contador)
    contador += 2


comando = ""

while comando != "salir":
    comando = input("$")
    print(comando)