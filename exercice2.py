# Additionne deux polynômes dans Z/2Z
def somPoly(P, Q):
    longueur_max = max(len(P), len(Q))
    P.extend([0] * (longueur_max - len(P)))
    Q.extend([0] * (longueur_max - len(Q)))
    return [(P[i] + Q[i]) % 2 for i in range(longueur_max)]

# Multiplie deux polynômes dans Z/2Z
def multPoly(P, Q):
    resultat = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            resultat[i + j] ^= P[i] & Q[j]
    return resultat

# Retourne le degré d'un polynôme
def degPoly(P):
    for i in reversed(range(len(P))):
        if P[i] != 0:
            return i
    return -1

# Divise le polynôme P par Q dans Z/2Z, renvoie le quotient et le reste.
def divPoly(P, Q):
    if degPoly(Q) == -1:
        raise ValueError("Division par zéro")
    quotient = [0] * (degPoly(P) - degPoly(Q) + 1)
    while degPoly(P) >= degPoly(Q):
        diff = degPoly(P) - degPoly(Q)
        P = somPoly(P, multPoly(Q, [0] * diff + [1]))
        quotient[diff] = 1
    return quotient, P

# Algorithme d'Euclide étendu pour les polynômes dans Z/2Z
def euclideEtendu(A, B):
    x, ancien_x = [0], [1]
    while degPoly(B) >= 0:
        quotient, reste = divPoly(A, B)
        A, B = B, reste
        x, ancien_x = somPoly(ancien_x, multPoly(quotient, x)), x
    return ancien_x

# Trouve l'inverse d'un polynôme P modulo poly_mod
def inverse_polynome(P, poly_mod):
    return euclideEtendu(poly_mod, P)

# Polynôme irréductible pour F_2^8 donnée dans l'exercice 
polyirreduc = [1, 1, 0, 1, 1, 0, 0, 0, 1] # X^8 + X^4 + X^3 + X + 1

# Création de la table des inverses
tableInverse = {}
for i in range(1, 256):
    binaire = [int(chiffre) for chiffre in bin(i)[2:]]
    P = [0] * (8 - len(binaire)) + binaire
    inv = inverse_polynome(P, polyirreduc)
    tableInverse[tuple(P)] = tuple(inv)

# Affichage des éléments de la table
for i, (P, inv) in enumerate(tableInverse.items()):
    print(f"P: {P}, Inverse: {inv}")
