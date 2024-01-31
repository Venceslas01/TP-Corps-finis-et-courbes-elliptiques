import random

# Paramètres de la courbe elliptique et du corps fini
p = 1019
a, b = 23, 39

# Vérifie si y est un résidu quadratique.
def verifieRes(y):
    return pow(y, (p - 1) // 2, p) == 1

#Trouve un point aléatoire sur la courbe elliptique.
def trouvPoint():
    while True:
        x = random.randint(0, p - 1)
        y_carre = (x**3 + a * x + b) % p
        if verifieRes(y_carre):
            y = pow(y_carre, (p + 1) // 4, p)
            return (x, y)

# Effectue l'addition de deux points sur la courbe.
def sommePoints(P, Q):

    if P == Q:
        if P[1] == 0:
            return None  # Point à l'infini
        lam = (3 * P[0]**2 + a) * pow(2 * P[1], -1, p) % p
    else:
        if P[0] == Q[0]:
            return None  # Point à l'infini
        lam = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p

    x3 = (lam**2 - P[0] - Q[0]) % p
    y3 = (lam * (P[0] - x3) - P[1]) % p
    return (x3, y3)

# Détermine l'ordre d'un point P sur la courbe.
def ordrePoint(P):
    ordre = 1
    Q = P
    while Q is not None:
        Q = sommePoints(Q, P)
        ordre += 1
        if Q == P:
            break
    return ordre

# Compte le nombre de points sur la courbe.
def comptPoints():
    
    nb_points = 1  # Incluant le point à l'infini
    for x in range(p):
        y_carre = (x**3 + a * x + b) % p
        if verifieRes(y_carre):
            nb_points += 2
    return nb_points

# Question 1
print("Question 1")
point = trouvPoint()
print("Point aléatoire sur la courbe :", point)

# Question 2
print("Question 2")
ordre = ordrePoint(point)
print("Ordre de ce point :", ordre)

# Question 3
print("Question 3")
total = comptPoints()
print("Nombre total de points sur la courbe :", total)
