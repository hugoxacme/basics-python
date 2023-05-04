#Operador Ternario

sabor_helado = input("Que sabor quieres?")

precio_helado = 15 if sabor_helado == "Vainilla" else "Compra otra cosa"

print(f'El Helado de vainilla cuesta {precio_helado}')


edad = 18

mensaje = "Ya pudes votar" if edad >= 18 else "Aun no puedes votar"

print(mensaje)