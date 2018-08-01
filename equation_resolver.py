from math import sqrt


def equazione2(a, b, c):
    delta = pow(b, 2) - 4 * a * c

    if a == 0:
        if b == 0 and c != 0:
            print("impossibile")

        elif (b != 0 and c == 0):
            print("L'unica soluzione è 0")

        elif (b == 0 and c == 0):
            print("L'equazione è indeterminata")

        else:
            return -c / b
    else:
        if delta > 0:  # parentesi e spazi

            x1 = (-b + sqrt(delta)) / (2 * a)  # dichiarazione variabili
            x2 = (-b - sqrt(delta)) / (2 * a)

            return (x1, x2)

        elif delta == 0:

            x1 = -b / (2 * a)

            print("L'unica soluzione è x1")

            return x1

        else:
            delta = delta * (-1)

            Re = -b / (2 * a)
            Im = sqrt(delta) / (2 * a)

            values = {"Re": Re,
                      "Im": Im}

            print("L'equazione da risultati in campo complesso")

            print("x1 =" " " + str(values["Re"]) + "+" + str(values["Im"]) + "j")
            print("x2 =" " " + str(values["Re"]) + "-" + str(values["Im"]) + "j")