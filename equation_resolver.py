from math import sqrt


def equazione2(a, b, c):
    delta = pow(b, 2) - 4 * a * c

    if a == 0:
        if b == 0 and c != 0:
            print("impossibile")

            return -1

        elif (b != 0 and c == 0):
            x1 = 0

            print("L'unica soluzione è" + x1)

            return x1

        elif (b == 0 and c == 0):
            print("L'equazione è indeterminata")

            return -1

        else:
            x1 = -c / b

            print("L'unica soluzione è " + x1)

            return x1
    else:
        if delta > 0:

            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)

            return x1, x2

        elif delta == 0:

            x1 = -b / (2 * a)

            print("L'unica soluzione è " + x1)

            return x1

        else:
            delta = delta * (-1)

            re = -b / (2 * a)
            im = sqrt(delta) / (2 * a)

            values = {"Re": re,
                      "Im": im}

            print("L'equazione da risultati in campo complesso")

            # https://stackoverflow.com/questions/7746143/formatting-complex-numbers
            # https://stackoverflow.com/questions/24669964/pretty-printing-of-complex-numbers
            print("x1 =" " " + str(values["Re"]) + "+" + str(values["Im"]) + "j")
            print("x2 =" " " + str(values["Re"]) + "-" + str(values["Im"]) + "j")

            # Compiti a casa :-)
            # return ???