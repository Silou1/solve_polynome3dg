# commentaire
# resolution approchée d'une equation du troisième degre
# version 2

import math

# Fonction calcul de delta


def calculerDelta(a, b, c):
    return b**2-4*a*c

# Fonction Résolution Equation Second Degre


def resoudreEquationSecondDegre(a, b, c):
    delta = calculerDelta(a, b, c)
    if delta > 0:
        racineDeDelta = math.sqrt(delta)
        retour = [(-b-racineDeDelta)/(2*a), (-b+racineDeDelta)/(2*a)]
    elif delta < 0:
        retour = []  # liste vide
    else:
        retour = [-b/(2*a)]  # liste d'un seul élément
    return retour

# Fonction qui calcule la faleur de f(x)=a^3 + bx^2 + cx + d


def calculerFxPolynome3dg(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


# Fonction qui permet de comparer le signe de deux nombre. true = de même signe, false = de signe opposé


def compareSign(x, y):
    if(x > 0 and y > 0) or (x < 0 and y < 0):
        return True
    else:
        return False

# Fonction qui itére 100 fois entre deux valeurs x1 et x2 avec f(x1) et f(x2) de signe opposé et retournant la valeur x approchant de f(x)=0


def trouverFxEgal0(p1, p2, a, b, c, d):
    for i in range(0, 100):
        # Pour cela, prenons un point p0 milieu p1 et p2 et regardons si il est positif ou négatif
        p0 = (p1+p2)/2
        # calculons f(p0), f(p1) et f(p2)
        fp0 = calculerFxPolynome3dg(p0, a, b, c, d)
        fp1 = calculerFxPolynome3dg(p1, a, b, c, d)
        fp2 = calculerFxPolynome3dg(p2, a, b, c, d)
        # print("itération ", i, " : fp0 = ", fp0," fp1 = ", fp1, " fp2 = ", fp2)
        if compareSign(fp0, fp1):
            p1 = p0
            p2 = p2
        else:
            p1 = p1
            p2 = p0

    return p0


# saisie des paramètres de la fonction f à l'aide de la fonction input
# input donnant une variable de type string, la fonction float la transforme en
# type décimale
print("Saisir les paramètres a,b,c,d de votre polynome du troisième degré a^3 + bx^2 + cx + d:")
a = float(input("Saisir la valeur de a="))
b = float(input("Saisir la valeur de b="))
c = float(input("Saisir la valeur de c="))
d = float(input("Saisir la valeur de d="))

# Calcul des paramètres de la fonction dérivée f'
A = 3*a
B = 2*b
C = c
print("La dérivée f' de la fonction f est ", A, "x^2 + ", B, "x + ", C)

# Calcul et affichage de l'équation du second degré f'
print("Résolution de l'équation f' ", A, "x^2 + ", B, "x + ", C)

delta = calculerDelta(A, B, C)
result = resoudreEquationSecondDegre(A, B, C)

# Condition sur delta de f' dans cet ordre >0 puis ==0 puis <0
if delta > 0:

    # Ordonnons les résultats x1 et x2, solution de l'équation f'(x)=0
    if result[0] > result[1]:
        x1 = result[1]
        x2 = result[0]
    else:
        x1 = result[0]
        x2 = result[1]

    print("Delta de f' est positif donc il y a 2 solutions")
    print("x1 =", x1)
    print("x2 =", x2)

    # Déterminons les variations de f selon la valeur de Delta et le signe de A
    if A > 0:
        print("Delta de f' est positif ainsi que A donc les variations de f(x) sont les suivantes :")
        print("pour x < ", x1, " f(x) est croissante")
        print("pour ", x1, " < x < ", x2, " f(x) est decroissante")
        print("pour x > ", x2, " f(x) est croissante")

    else:  # A est négatif
        print("Delta de f' est positif et A est négatif donc les variations de f(x) sont les suivantes :")
        print("pour x < ", result[0], " f(x) est décroissante")
        print("pour ", result[0], " < x < ", result[1], " f(x) est croissante")
        print("pour x > ", result[1], " f(x) est décroissante")

    # Calculons f(x1) et f(x2), extremums de f pour Delta > 0 et A positif ou négatif
    print("Calculons f(x1) et f(x2), extremum de f")
    f1 = calculerFxPolynome3dg(x1, a, b, c, d)
    f2 = calculerFxPolynome3dg(x2, a, b, c, d)

    print("f1 =", f1)
    print("f2 =", f2)

    if (f1 < 0 and f2 > 0) or (f1 > 0 and f2 < 0):

        print("Cas ou f1 et f2 sont de signes oposés. Il y a donc une solution f(x) = 0 pour x compris entre x1 et x2")

        # Approchons la solution f(x) = 0 pour x compris entre x1 et x2
        # ---------------------------------------------------------------

        # Faisons une boucle qui calcul f(x) pour x compris entre x1 et x2
        p1 = x1
        p2 = x2

        p0 = trouverFxEgal0(p1, p2, a, b, c, d)

        print(
            "Valeur approchant p0 de x pour f(x) = 0 et x compris entre x1 et x2 après n itérations : ", p0)
        print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))

        # Approchons la solution f(x) = 0 pour x < x1
        # ----------------------------------------------------

        # trouvons un point x0 inférieur à x1 de sorte que f(x0) soit de signe opposé à f(x1)
        x0 = x1 - 1

        while compareSign(calculerFxPolynome3dg(x0, a, b, c, d), calculerFxPolynome3dg(x1, a, b, c, d)):
            x0 = x0 - 1

        print(
            "Valeur de x0 de sorte que f(x0) et f(x1) soient de signe opposé avec x < x1 : ", x0)
        print("Valeur de f(x0) ", calculerFxPolynome3dg(x0, a, b, c, d))
        print("Valeur de f(x1) ", calculerFxPolynome3dg(x1, a, b, c, d))

        p0 = trouverFxEgal0(x0, x1, a, b, c, d)
        print(
            "Valeur approchant p0 de x pour f(x) = 0 et x < x1 après n itérations : ", p0)
        print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))

        # Approchons la solution f(x) = 0 pour x > x2
        # ----------------------------------------------------

        # trouvons un point x0 supérieur à x2 de sorte que f(x0) soit de signe opposé à f(x2)
        x0 = x2 + 1

        while compareSign(calculerFxPolynome3dg(x0, a, b, c, d), calculerFxPolynome3dg(x2, a, b, c, d)):
            x0 = x0 + 1

        print(
            "Valeur de x0 de sorte que f(x0) et f(x2) soient de signe opposé avec x > x2 : ", x0)
        print("Valeur de f(x0) ", calculerFxPolynome3dg(x0, a, b, c, d))
        print("Valeur de f(x2) ", calculerFxPolynome3dg(x1, a, b, c, d))

        p0 = trouverFxEgal0(x0, x2, a, b, c, d)
        print(
            "Valeur approchant p0 de x pour f(x) = 0 et x > x2 après n itérations : ", p0)
        print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))

    else:  # les extremums sont de mêmes signes
        print("Cas ou f1 et f2 sont de même signes. Il n'y a donc pas de solution f(x) = 0 pour x compris entre x1 et x2")

        if compareSign(f1, A):
            print(
                "f1 et A sont de même signe. Donc, il existe une solution x telle que f(x)=0 pour x < x1")

            # Approchons la solution f(x) = 0 pour x < x1
            # ----------------------------------------------------

            # trouvons un point x0 inférieur à x1 de sorte que f(x0) soit de signe opposé à f(x1)
            x0 = x1 - 1

            while compareSign(calculerFxPolynome3dg(x0, a, b, c, d), calculerFxPolynome3dg(x1, a, b, c, d)):
                x0 = x0 - 1

            print(
                "Valeur de x0 de sorte que f(x0) et f(x1) soient de signe opposé avec x < x1 : ", x0)
            print("Valeur de f(x0) ", calculerFxPolynome3dg(x0, a, b, c, d))
            print("Valeur de f(x1) ", calculerFxPolynome3dg(x1, a, b, c, d))

            p0 = trouverFxEgal0(x0, x1, a, b, c, d)
            print(
                "Valeur approchant p0 de x pour f(x) = 0 et x < x1 après n itérations : ", p0)
            print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))

        else:
            print(
                "f1 et A sont de signe opposé. Donc, il existe une solution x telle que f(x)=0 pour x > x2")

            # Approchons la solution f(x) = 0 pour x > x2
            # ----------------------------------------------------

            # trouvons un point x0 supérieur à x2 de sorte que f(x0) soit de signe opposé à f(x2)
            x0 = x2 + 1

            while compareSign(calculerFxPolynome3dg(x0, a, b, c, d), calculerFxPolynome3dg(x2, a, b, c, d)):
                x0 = x0 + 1

            print(
                "Valeur de x0 de sorte que f(x0) et f(x2) soient de signe opposé avec x > x2 : ", x0)
            print("Valeur de f(x0) ", calculerFxPolynome3dg(x0, a, b, c, d))
            print("Valeur de f(x2) ", calculerFxPolynome3dg(x1, a, b, c, d))

            p0 = trouverFxEgal0(x0, x2, a, b, c, d)
            print(
                "Valeur approchant p0 de x pour f(x) = 0 et x > x2 après n itérations : ", p0)
            print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))

else:  # Delta est null ou négatif

    if delta == 0:
        print("Delta de f' est nul donc il y a 1 solution unique")
        print("x0 =", result[0])

        # Déterminons les variations de f selon la valeur de Delta et le signe de A
        if A > 0:
            print("Delta de f' est null et A est postif donc f est toujours croissante")
        else:  # A est négatif
            print(
                "Delta de f' est null et A est négatif donc f est toujours décroissante")

    else:
        print("Pas de solution dans l'espace des réel pour f'(x)=0")

        # Déterminons les variations de f selon la valeur de Delta et le signe de A
        if A > 0:
            print(
                "Delta de f' est négatif et A est postif donc f est toujours croissante")
        else:  # A est négatif
            print(
                "Delta de f' est négatif et A est négatif donc f est toujours décroissante")

    # Trouvons une valeur de x tel que f(0) et f(x) soit de signe opposé.
    # Pour cela, comparons le signe de A et de d pour détermine si x pour f(x)=0 est positif ou négatif

    if compareSign(A, d):
        # Approchons la solution f(x) = 0 pour x < 0
        # ----------------------------------------------------

        # trouvons un point x0 inférieur à x1 de sorte que f(x0) soit de signe opposé à f(x1)
        x0 = - 1

        while compareSign(calculerFxPolynome3dg(x0, a, b, c, d), d):
            x0 = x0 - 1

        print(
            "Valeur de x0 de sorte que f(x0) et d soient de signe opposé avec x < 0 : ", x0)
        print("Valeur de f(x0) ", calculerFxPolynome3dg(x0, a, b, c, d))

        p0 = trouverFxEgal0(x0, 0, a, b, c, d)
        print(
            "Valeur approchant p0 de x pour f(x) = 0 et x < 0 après n itérations : ", p0)
        print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))
    else:
        # Approchons la solution f(x) = 0 pour x > 0
        # ------------------------------------------

        # trouvons un point x0 supérieur à x2 de sorte que f(x0) soit de signe opposé à f(x2)
        x0 = 1

        while compareSign(calculerFxPolynome3dg(x0, a, b, c, d), d):
            x0 = x0 + 1

        print(
            "Valeur de x0 de sorte que f(x0) et d soient de signe opposé avec x > 0 : ", x0)
        print("Valeur de f(x0) ", calculerFxPolynome3dg(x0, a, b, c, d))

        p0 = trouverFxEgal0(x0, 0, a, b, c, d)
        print(
            "Valeur approchant p0 de x pour f(x) = 0 et x > 0 après n itérations : ", p0)
        print("Valeur de f(p0): ", calculerFxPolynome3dg(p0, a, b, c, d))
