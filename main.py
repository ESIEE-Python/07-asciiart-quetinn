"""
asciiart
"""
#### Imports et définition des variables globales


#### Fonctions secondaires

import sys
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    c = [s[0]]
    o = [1]
    n = len(s)
    for i in range(1,n):
        if s[i] == s[i-1]:
            o[-1] += 1
        else:
            o.append(1)
            c.append(s[i])
    l=list(zip(c,o,strict = True))
    return l


sys.setrecursionlimit(4000)
def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

# Votre fonction récursive

# Fonction récursive pour coder la chaîne de caractères
    if not s:
        return []

    def encode_recursive(substring, current_char, count):
        if not substring:
            return [(current_char, count)]

        if substring[0] == current_char:
            return encode_recursive(substring[1:], current_char, count + 1)
        return [(current_char, count)] + encode_recursive(substring[1:], substring[0], 1)

    return encode_recursive(s[1:], s[0], 1)


#### Fonction principale
def main():
    """ appel fonction
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
if __name__ == "__main__":
    main()
