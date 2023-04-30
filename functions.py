#funcion
def hello_world():
    print('Hello world!') 
#Funciones args
def hello_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]

    print(f'Hello, {first_name}, {second_name}, {third_name}')
#funciones con parametro
def name(first_name):
    print(f"Hello, {first_name}")


#kwargs
def kwarg(first, second):
    print(f"Hello, {first} {second}")


def akwarg(**kwargs):
    if kwargs.get('second_person') is None:
        print("No hay segunda persona")
    else:
        print(f"hello, {kwargs['first_person']} / {kwargs['second_person']}")

    


#name("hugo")
#hello_args('Hugo', "paco", "luis")
#kwarg(first="Hugo", second="Acosta")
akwarg(first_person="hugo",) #second_person="karime")