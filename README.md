# TP Corps Finis et Courbes Elliptiques
# Introduction

Ce travail pratique se concentre sur l'application des principes mathématiques liés aux corps finis et aux courbes elliptiques, en mettant en œuvre des algorithmes pour le calcul du plus grand commun diviseur (pgcd) de deux polynômes, la création d'une table des inverses dans un corps fini, et l'analyse de la structure d'une courbe elliptique.
Outils et Technologies Utilisés

    Langage de programmation :Python

# Exercice 1: Algorithme d'Euclide pour Polynômes

    Implémentation de l'Algorithme d'Euclide : Développement d'une fonction pour calculer le pgcd de deux polynômes P et Q dans Fp[X], où p est un nombre premier. L'algorithme suit une approche itérative, réduisant progressivement les polynômes jusqu'à obtenir le dernier reste non-nul comme pgcd.
    Extension de l'Algorithme d'Euclide : Adaptation de l'algorithme pour calculer également les polynômes U et V tels que D = PU + QV, où D est le pgcd de P et Q. Cette méthode permet de représenter le pgcd comme une combinaison linéaire des polynômes initiaux.

# Exercice 2: Table des Inverses dans F2m

    Calcul des Inverses : Création d'une table d'inverses pour les éléments du corps fini F2m, en utilisant le polynôme X^8 + X^4 + X^3 + X + 1 pour structurer le corps. Cette partie implique la manipulation de polynômes modulo un polynôme irréductible pour trouver les inverses de chaque élément.

# Exercice 3: Courbe Elliptique sur IF1019

    Point Aléatoire sur la Courbe : Écriture d'une fonction pour générer un point aléatoire sur la courbe elliptique y^2 = x^3 + 23x + 39 définie sur IF1019. Analyse de l'ordre du point généré pour en déduire des informations sur la structure du groupe de points de la courbe.
    Calcul du Nombre de Points : Détermination du nombre total de points de la courbe elliptique définis sur IF1019, en utilisant des méthodes de calcul numérique et théorique pour évaluer la cardinalité du groupe de points.

# Conclusion

À travers ce TP, j'ai pu explorer en détail les applications pratiques des corps finis et des courbes elliptiques, renforçant ainsi ma compréhension des concepts cryptographiques et des structures algébriques. Les compétences acquises constituent une base solide pour l'approfondissement futur dans la cryptographie.
