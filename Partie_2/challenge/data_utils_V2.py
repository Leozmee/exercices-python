def somme_cumulee(liste):
    resultat = []
    total = 0
    for valeur in liste:
        total += valeur
        resultat.append(total)
    return resultat


def compter_occurrences(liste):
    occurrences = {}
    for i in liste:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    return occurrences


def inverser_dict(dictionnaire):
    inverse = {}
    for cle, valeur in dictionnaire.items():
        inverse[valeur] = cle
    return inverse


def filtrer_pairs(liste):
    pairs = []
    for nombre in liste:
        if nombre % 2 == 0:
            pairs.append(nombre)
    return pairs


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def trouver_doublons(liste):
    parcouru = []
    doublons = []
    for i in liste:
        if i in parcouru and i not in doublons:
            doublons.append(i)
        parcouru.append(i)
    return doublons


def calculer_moyenne_ponderee(valeurs, poids):
    total = 0
    for i in range(len(valeurs)):
        total += valeurs[i] * poids[i]
    return total / sum(poids)
