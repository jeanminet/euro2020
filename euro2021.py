import random

Z = 0
n = 10000

def match(P,S,p,j,e1,e2):
    if S[p][e1][j] == -1 or S[p][e2][j] == -1:
        return P
    elif S[p][e1][j] > S[p][e2][j]:
        P[p][e1] += 3
    elif S[p][e1][j] < S[p][e2][j]:
        P[p][e2] += 3
    else:
        P[p][e1] += 1
        P[p][e2] += 1
    P[p][e1] += 0.01 * (S[p][e1][j] - S[p][e2][j])
    P[p][e2] += 0.01 * (S[p][e2][j] - S[p][e1][j])
    return P

def flatten(X):
    F = [0]*24
    for i in range(6):
        for j in range(4):
            F[4*i+j] = X[i][j]
    return F


for t in range(n):

    G = [[]*4 for i in range(6)]
    G[0] = ["Turquie", "Italie", "Pays de Galles", "Suisse"]
    G[1] = ["Danemark", "Finlande", "Belgique", "Russie"]
    G[2] = ["Pays-Bas", "Ukraine", "Autriche", "Macédoine du Nord"]
    G[3] = ["Angleterre", "Croatie", "Ecosse", "République tchèque"]
    G[4] = ["Espagne", "Suède", "Pologne", "Slovaquie"]
    G[5] = ["Hongrie", "Portugal", "France", "Allemagne"]

    P = [[0]*4 for i in range(6)]
    S = [[[0]*3 for i in range(4)] for j in range(6)]

    S[0][0] = [0,0,-1]
    S[0][1] = [3,3,-1]
    S[0][2] = [1,2,-1]
    S[0][3] = [1,0,-1]

    S[1][0] = [0,1,-1]
    S[1][1] = [1,0,-1]
    S[1][2] = [3,2,-1]
    S[1][3] = [0,1,-1]

    S[2][0] = [3,2,-1]
    S[2][1] = [2,2,-1]
    S[2][2] = [3,0,-1]
    S[2][3] = [1,1,-1]

    S[3][0] = [1,0,-1]
    S[3][1] = [0,1,-1]
    S[3][2] = [0,0,-1]
    S[3][3] = [2,1,-1]

    S[4][0] = [0,1,-1]
    S[4][1] = [0,1,-1]
    S[4][2] = [1,1,-1]
    S[4][3] = [2,0,-1]

    S[5][0] = [0,1,-1]
    S[5][1] = [3,2,-1]
    S[5][2] = [1,1,-1]
    S[5][3] = [0,4,-1]

    for p in range(6):
        # journee 1
        P = match(P,S,p,0,0,1)
        P = match(P,S,p,0,2,3)
        # journee 2
        P = match(P,S,p,1,0,2)
        P = match(P,S,p,1,1,3)

    for i in range(1):
        # Random draw of still unplayed matches
        for p in range(6):
            for e in range(4):
                for j in range(3):
                    if S[p][e][j] == -1:
                        S[p][e][j] = random.randint(0,7)
        
        #S[5][2][2] = 0
        #S[5][1][2] = 7

        for p in range(6):
            # journée 3
            P = match(P,S,p,2,0,3)
            P = match(P,S,p,2,1,2)

        Gf = flatten(G)
        P = flatten(P)

        rank = sorted(range(24), key=lambda k: P[k])
        A = [Gf[i] for i in rank].index("France")
        if A <= 7:
            Z += 1

print(Z/n*100)