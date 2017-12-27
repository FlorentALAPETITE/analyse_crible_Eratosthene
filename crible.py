#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en paramètre
# Par exemple :    cribleEratosthene(120)


def cribleEratosthene(n):
    listeNombres = list(range(2, n + 1))  # Liste des nombres de 2 à n compris
    nombresPremiers = set()  # Ensemble de retour

    # Tant que la liste des nombres n'est pas vide
    while len(listeNombres) != 0:
        nombreCourant = listeNombres[0]
        nombresPremiers.add(nombreCourant)  # Le nombre courant est premier
        listeNombres.remove(nombreCourant)  # On retire l'élément courant de la liste

        # Création d'une nouvelle liste sans les nombres divisibles par le nombre courant
        listeNombres = [nombre for nombre in listeNombres if nombre % nombreCourant != 0]

    return nombresPremiers



#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en paramètre
# Par exemple :    cribleEratosthene(120)


# Ce code est absolument crade
def cribleEratosthene_degeu(n):

    # Liste des nombres de 2 à n compris (dégeu)
    listeNombres = []
    for i in range(1, n):
        tmp = i + 1
        listeNombres.append(tmp)

    nombresPremiers = []  # Liste de retour

    listePasBon = []

    i = 0

    # Tant que la liste des nombres n'est pas complètement parcourue (condition crade)
    while (len(nombresPremiers) + len(listePasBon)) != len(listeNombres):
        nombreCourant = listeNombres[i]

        # Test dégeu pour savoir si le nombre courant est premier
        if(nombreCourant not in listePasBon):
            nombresPremiers.append(nombreCourant)  # Le nombre courant est premier

            # Boucle dégeu sur tous les nombres
            for nombre in listeNombres:

                # Test dégeu pour savoir si le nombre parcouru n'est pas premier
                if nombre != nombreCourant and nombre not in listePasBon and nombre % nombreCourant == 0:
                    listePasBon.append(nombre)
        i = i + 1

    return nombresPremiers

