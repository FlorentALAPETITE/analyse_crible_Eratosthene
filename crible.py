import time

#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en parametre
# Par exemple :    cribleEratosthene(120)


def cribleEratosthene(n):
    listeNombres = list(range(2, n + 1))  # Liste des nombres de 2 a n compris
    nombresPremiers = set()  # Ensemble de retour

    # Tant que la liste des nombres n'est pas vide
    while len(listeNombres) != 0:
        nombreCourant = listeNombres[0]
        nombresPremiers.add(nombreCourant)  # Le nombre courant est premier
        listeNombres.remove(nombreCourant)  # On retire l'element courant de la liste

        # Creation d'une nouvelle liste sans les nombres divisibles par le nombre courant
        listeNombres = [nombre for nombre in listeNombres if nombre % nombreCourant != 0]

    return nombresPremiers



#NOMS DES PARTICIPANTS : BRASSIER / LARDY / LE FALHUN

def creation_tab(n):

    T = [i for i in range(2, n+1)]

    return T


def divisible(i,n):

    if n % i == 0 and i != n:

        return(True)

    else:

        return(False)

        

def eratosthene(n):

    T = creation_tab(n)

    for i in T : 

        for n in T : 

            if divisible(i,n):

                T.remove(n)

    return T


# Fonction d'analyse de temps d'exécution

def analyse(params):
    functions = [cribleEratosthene, eratosthene]
    res = []
    for func in functions:
        inner = []
        for p in params:
            start = time.time()
            func(p)
            end = time.time()
            print(func, p, end - start)
            inner.append(end - start)
        res.append(inner)

    return res
