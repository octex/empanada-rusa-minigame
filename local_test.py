from random import randrange, choice

AMOUNT_EMPANADAS = 4
GOOD_EMPANADAS = ("carne a cuchillo", "jamon y queso", "humita", "carne picante", "atun",
                  "caprese", "roquefort con jamon", "pollo", "verdura", "carne suave",
                  "panceta y ciruela", "queso al verdeo")
BAD_EMPANADAS = ("culo", "cemento", "caca", "vomito", "pegamento", "merca", "waska",
                 "barro", "menarca", "plomo", "pelos anales", "vello pubico", "clavos",
                 "pija", "prensado")


#class Player:
#    def __init__(self, name, address):
#        self.name = name
#        self.address = address


class Empanada:
    def __init__(self, is_bad=False):
        self.is_bad = is_bad
        if self.is_bad:
            self.taste = choice(BAD_EMPANADAS)
        else:
            self.taste = choice(GOOD_EMPANADAS)
    def get_type(self):
        return self.taste
    def is_the_bad_one(self):
        return self.is_bad

def check_if_only_one(empanadas):
    counter = 0
    for empanada in empanadas:
        if empanada is not None:
            counter += 1
    return counter == 1


def generate_emp(amount):
    tmp_empanadas = []
    random_bad = randrange(amount)
    for _ in range(amount):
        if _ == random_bad:
            temp_emp = Empanada(is_bad=True)
            tmp_empanadas.append(temp_emp)
        else:
            temp_emp = Empanada()
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
                if empanada_elegida.is_the_bad_one():
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


