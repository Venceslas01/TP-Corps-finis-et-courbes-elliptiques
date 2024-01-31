

def soustPoly(p1, p2, p):
    while len(p1) < len(p2):
        p1.insert(0, 0)
    while len(p2) < len(p1):
        p2.insert(0, 0)
    # Soustraction des coefficients des polynômes modulo p
    return [(a - b) % p for a, b in zip(p1, p2)]



 # Calcul du PGCD des polynômes 
def pgcdPoly(p1, p2, p):
    while any(coeff != 0 for coeff in p2):
        # Réduction de p1 modulo p2 jusqu'à ce que la longueur de p1 soit inférieure 
        while len(p1) >= len(p2) and any(coeff != 0 for coeff in p1):
            # Calcul du facteur de réduction
            facteur = (p1[0] * pow(p2[0], p - 2, p)) % p
            # Réduction de p1 par p2
            reduction = [(coeff * facteur) % p for coeff in p2] + [0] * (len(p1) - len(p2))
            p1 = [(a - b) % p for a, b in zip(p1, reduction)]
            # Élimination des zéros en tête de p1
            while p1 and p1[0] == 0:
                p1.pop(0)

        # Échanger p1 et p2 pour la prochaine itération
        p1, p2 = p2, p1

    return p1 # Retour du PGCD

def multiPoly(p1, p2, p):
    # Initialiser le résultat avec des zéros
    resultat = [0] * (len(p1) + len(p2) - 1)
    # Multiplication de chaque terme de p1 par chaque terme de p2
    for i in range(len(p1)):
        for j in range(len(p2)):
            resultat[i + j] = (resultat[i + j] + p1[i] * p2[j]) % p
    return resultat

def euclideEtenduPoly(P, Q, p):
    # Initialiser U, V
    U, V, U1, V1 = [1], [0], [0], [1]

    # Itérer tant que Q n'est pas le polynôme nul
    while any(Q):
        # Diviser P par Q
        quotient, reste = divPoly(P, Q, p)

        # Mise à jour de P, Q pour la prochaine itération
        P, Q = Q, reste

        # Mise à jour de U, V, U1, V1
        U, U1 = U1, soustPoly(U, multiPoly(quotient, U1, p), p)
        V, V1 = V1, soustPoly(V, multiPoly(quotient, V1, p), p)

    return U, V 




def divPoly(P, Q, p):
    # Vérifier que le diviseur Q n'est pas le polynôme nul
    if not Q or Q[0] == 0:
        raise ValueError("Division par un polynôme nul")

    quotient = [0] * (len(P) - len(Q) + 1)
    while len(P) >= len(Q) and P[0] != 0:
        # Calculer le facteur du terme de tête pour la soustraction
        facteur = (P[0] * pow(Q[0], p - 2, p)) % p
        # Réduire le polynôme P
        reduction = [(coeff * facteur) % p for coeff in Q] + [0] * (len(P) - len(Q))
        P = soustPoly(P, reduction, p)
        while P and P[0] == 0:
            P.pop(0)
        if len(P) - len(Q) >= 0:
            quotient[len(P) - len(Q)] = facteur

    return quotient, P


p = 5  # Nombre premier pour le corps fini Fp
p1 = [3,4,1]  
p2 = [2,1]   

pgcd = pgcdPoly(p1, p2, p)
U, V = euclideEtenduPoly(p1,p2, p)

# Question 1
print("Question 1")
print("Le PGCD des polynômes est :", pgcd)

# Question 2
print("Question 2")
print("U:", U)
print("V:", V)
