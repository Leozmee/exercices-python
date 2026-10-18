PI = 3.14159
E = 2.71828  

def carre(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

def valeur_absolue(x):
    if x < 0:
        return -x
    return x

def maximum(liste):
    plus_grand = liste[0]
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand

def minimum(liste):
    plus_petit = liste[0]
    for valeur in liste:
        if valeur < plus_petit:
            plus_petit = valeur
    return plus_petit

def moyenne(liste):
    return sum(liste) / len(liste)

def ecart_type(liste):
    m = moyenne(liste)
    variance = sum((valeur - m) ** 2 for valeur in liste) / len(liste)
    return variance ** 0.5

def mediane(liste):
    triee = sorted(liste)
    n = len(triee)
    milieu = n // 2
    if n % 2 == 1:
        return triee[milieu]
    return (triee[milieu - 1] + triee[milieu]) / 2
