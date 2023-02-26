import random

def demander_nombre(nb_min, nb_max):

    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input('quel est le nombre magique (entre %s et %s)' % (nb_min, nb_max))
        try:
            nombre_int = int(nombre_str)
        except:
            print('un nombre idiot')
        else:
            if nombre_int < NOMBRE_MIN or nombre_int > NOMBRE_MAX:
                print('entre 1 et 10 le nombre')
                nombre_int = 0

    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(1, 10)
NOMBRE_DE_VIE = 4
nombre = 0
vie = NOMBRE_DE_VIE

while not nombre == NOMBRE_MAGIQUE and vie > 0:
    print(f'il vous reste {vie} vies')

    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")

    elif nombre > NOMBRE_MAGIQUE:
        print('le nombre magique est plus petit')
        vie -= 1

    else:
        print("le nombre magique est plus grand")
        vie -= 1

if vie == 0: print(f"Vous avez perdu, le nombre magique était: {NOMBRE_MAGIQUE}")
