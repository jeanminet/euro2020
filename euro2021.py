import random
import datetime

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

# 6 groups of 4 teams
G = [[]*4 for i in range(6)]
G[0] = ["Turquie", "Italie", "Pays de Galles", "Suisse"]
G[1] = ["Danemark", "Finlande", "Belgique", "Russie"]
G[2] = ["Pays-Bas", "Ukraine", "Autriche", "Macédoine du Nord"]
G[3] = ["Angleterre", "Croatie", "Ecosse", "République tchèque"]
G[4] = ["Espagne", "Suède", "Pologne", "Slovaquie"]
G[5] = ["Hongrie", "Portugal", "France", "Allemagne"]
Gf = flatten(G)

qualified = [0]*24

for t in range(n):

    P = [[0]*4 for i in range(6)]
    S = [[[0]*3 for i in range(4)] for j in range(6)]

    # Group 1
    S[0][0] = [0,0,1]
    S[0][1] = [3,3,1]
    S[0][2] = [1,2,0]
    S[0][3] = [1,0,3]

    # Group 2
    S[1][0] = [0,1,-1]
    S[1][1] = [1,0,-1]
    S[1][2] = [3,2,-1]
    S[1][3] = [0,1,-1]

    # Group 3
    S[2][0] = [3,2,-1]
    S[2][1] = [2,2,-1]
    S[2][2] = [3,0,-1]
    S[2][3] = [1,1,-1]

    # Group 4 
    S[3][0] = [1,0,-1]
    S[3][1] = [0,1,-1]
    S[3][2] = [0,0,-1]
    S[3][3] = [2,1,-1]

    # Group 5
    S[4][0] = [0,1,-1]
    S[4][1] = [0,1,-1]
    S[4][2] = [1,1,-1]
    S[4][3] = [2,0,-1]

    # Group 6
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

    # Random draw of still unplayed matches
    for p in range(6):
        for e in range(4):
            for j in range(3):
                if S[p][e][j] == -1:
                    S[p][e][j] = random.randint(0,7)

    for p in range(6):
        # journée 3
        P = match(P,S,p,2,0,3)
        P = match(P,S,p,2,1,2)


    P = flatten(P)

    rank = sorted(range(24), key=lambda k: P[k])
    for r in rank[8:24]:
        qualified[r] += 1
    
rank = sorted(range(24), key=lambda k: qualified[k])

print("Probability of team being qualified ({})".format(datetime.date.today()))
for i in rank[::-1]:
    print("{} : {:.1f} %".format(Gf[i], qualified[i] / n * 100))