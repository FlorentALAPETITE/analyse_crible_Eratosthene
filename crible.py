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


#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en parametre
# Par exemple :    cribleEratosthene(120)


# Ce code est absolument crade
def cribleEratosthene_degeu(n):

    # Liste des nombres de 2 a n compris (degeu)
    listeNombres = []
    for i in range(1, n):
        tmp = i + 1
        listeNombres.append(tmp)

    nombresPremiers = []  # Liste de retour

    listePasBon = []

    i = 0

    # Tant que la liste des nombres n'est pas completement parcourue (condition crade)
    while (len(nombresPremiers) + len(listePasBon)) != len(listeNombres):
        nombreCourant = listeNombres[i]

        # Test degeu pour savoir si le nombre courant est premier
        if(nombreCourant not in listePasBon):
            nombresPremiers.append(nombreCourant)  # Le nombre courant est premier

            # Boucle degeu sur tous les nombres
            for nombre in listeNombres:

                # Test degeu pour savoir si le nombre parcouru n'est pas premier
                if nombre != nombreCourant and nombre not in listePasBon and nombre % nombreCourant == 0:
                    listePasBon.append(nombre)
        i = i + 1

    return nombresPremiers


def analyse():
    params = [10 ^ 2, 10 ^ 3, 10 ^ 4, 10 ^ 5, 10 ^ 6, 10 ^ 7]
    functions = [cribleEratosthene, cribleEratosthene_degeu]
    res = []
    for func in functions:
        inner = []
        for p in params:
            start = time.time()
            func(p)
            end = time.time()
            inner.append(end - start)
        res.append(inner)

    return res
