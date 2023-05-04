
#IF ejemolos
mascotas = ["Flaca", "Fina", "Calle", "Churrumai"]


if "Churrumai" in mascotas:
    print("Hola Churrumai")


edad = 15

if edad > 50:
    print("puedes entrar con descuento!")
elif edad >= 18:
    print("puedes entrar al cine")
else:
    print("Esta pelicula es para mayores de edad")




mandado = ["Leche", "Pan", "Huevo", "Harina", "Fruta"]

if "cereal" in mandado:
    print("Tambien traje cereal")
else:
    print("Olvide el cereal")


#Operador Ternario

#sabor_helado = input("Que sabor quieres?")

#precio_helado = 15 if sabor_helado == "Vainilla" else "Compra otra cosa"

#print(f'El Helado de vainilla cuesta {precio_helado}')


edad = 18

mensaje = "Ya pudes votar" if edad >= 18 else "Aun no puedes votar"

#print(mensaje)



#for loop range
#Sumar del 0 al 20
for numero in range(0, 20, 2):
    print(numero + 2)

for numero in range(5):
    print(numero + 1)





#while