from itertools import permutations

def lex_per(cadena:str):
    perm = sorted(''.join(c) for c in permutations(cadena))
    for i in perm:
        print(i)

