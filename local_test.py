from random import randrange

AMOUNT_EMPANADAS = 4


class Empanada:
    def __init__(self, type, is_it=False):
        self.type = type
        self.is_it = is_it
    def get_type(self):
        return self.type
    def is_the_one(self):
        return self.is_it

def check_if_only_one(empanadas):
    counter = 0
    for empanada in empanadas:
        if empanada is not None:
            counter += 1
    if counter == 1:
        return True
    else:
        return False


def generate_emp(amount):
    tmp_empanadas = []
    random_bad = randrange(amount)
    for _ in range(amount):
        if _ == random_bad:
            temp_emp = Empanada(type="CULO", is_it=True)
            tmp_empanadas.append(temp_emp)
        else:
            temp_emp = Empanada(type="carne")
            tmp_empanadas.append(temp_emp)
    return tmp_empanadas

print("Que onda wachin! Bienvenido a la casa de empandas")
print(f"Te vamos a traer {AMOUNT_EMPANADAS} empanadas")
print("Vas a tener que elegir una, pero ojo! Una tiene sabor a culo")
print("Para elegir, ingresa el numero de empanada teniendo en cuenta la cantidad maxima")
print("Suerte UwU")
empanadas = generate_emp(amount=AMOUNT_EMPANADAS)

while True:
    choice = input("Tu empanada: ")
    try:
        choice = int(choice)
        if choice > len(empanadas):
            print("Te fuiste a la verga, tampoco tenemos tantas")
        elif choice <= 0:
            print("No lo vas a buguear ;)")
        else:
            tmp_index = choice - 1
            empanada_elegida = empanadas[tmp_index]
            try:
                empanada_elegida_sabor = empanada_elegida.get_type()
                if empanada_elegida.is_the_one():
                    print(f"Noooooooo te comiste la empanada de {empanada_elegida_sabor}!!!!11!1")
                    print("Malardo amigo")
                    print("************************GAME OVER************************")
                    break
                else:
                    print(f"Safaste rey! Era solo una empanada de {empanada_elegida_sabor}")
                    empanadas[tmp_index] = None
                    if check_if_only_one(empanadas):
                        print("Te felicito amigo, te ganaste el pijazo de oro :D")
                        print("************************A WINNER IS YOU************************")
                        break
            except AttributeError:
                print("Esa ya la elegiste. No seas gil.")
    except ValueError:
        print("Amigo pusiste cualquiera, vamos de nuevo.")


