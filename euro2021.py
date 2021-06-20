import random
import datetime

# Estimate the probability of each teams being qualified by 
# Monte-Carlo simulation of the still unplayed matched

def scores():
    S = [[[0]*3 for i in range(4)] for j in range(6)]
    # Group 1
    S[0][0] = [0,0,1] # Turquie
    S[0][1] = [3,3,1] # Italie
    S[0][2] = [1,2,0] # Pays de Galles
    S[0][3] = [1,0,3] # Suisse

    # Group 2
    S[1][0] = [0,1,-1] # Danemark
    S[1][1] = [1,0,-1] # Finlande
    S[1][2] = [3,2,-1] # Belgique
    S[1][3] = [0,1,-1] # Russie

    # Group 3
    S[2][0] = [3,2,-1] # Pays-bas
    S[2][1] = [2,2,-1] # Ukraine
    S[2][2] = [3,0,-1] # Autriche
    S[2][3] = [1,1,-1] # Macédoine du Nord

    # Group 4 
    S[3][0] = [1,0,-1] # Angleterre
    S[3][1] = [0,1,-1] # Croatie
    S[3][2] = [0,0,-1] # Ecosse
    S[3][3] = [2,1,-1] # République tchèque

    # Group 5
    S[4][0] = [0,1,-1] # Espagne
    S[4][1] = [0,1,-1] # Suède
    S[4][2] = [1,1,-1] # Pologne
    S[4][3] = [2,0,-1] # Slovaquie

    # Group 6
    S[5][0] = [0,1,-1] # Hongrie
    S[5][1] = [3,2,-1] # Portugal
    S[5][2] = [1,1,-1] # France
    S[5][3] = [0,4,-1] # Allemagne

    return S

def match(P,S,p,d,e1,e2):
    # Returns P that keeps track of the points earned by each team during a match
    # S: score of each team in each of the 3 days (d)
    # g: group index (between 0 and 5)
    # d: day index (between 0 and 2)
    # e1: team 1 index (between 0 and 3)
    # e2: team 2 index (between 0 and 3)
    if S[p][e1][d] == -1 or S[p][e2][d] == -1:
        # Match still unplayed
        return P
    elif S[p][e1][d] > S[p][e2][d]:
        P[p][e1] += 3
    elif S[p][e1][d] < S[p][e2][d]:
        P[p][e2] += 3
    else:
        P[p][e1] += 1
        P[p][e2] += 1
    # Count the goal difference as 1/100 of a point
    P[p][e1] += 0.01 * (S[p][e1][d] - S[p][e2][d])
    P[p][e2] += 0.01 * (S[p][e2][d] - S[p][e1][d])
    return P

def flatten(X):
    Xf = [0]*24
    for i in range(6):
        for j in range(4):
            Xf[4*i+j] = X[i][j]
    return Xf

n = 10000

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
    S = scores()

    # Random draw of still unplayed matches
    for p in range(6):
        for e in range(4):
            for d in range(3):
                if S[p][e][d] == -1:
                    # Draw a score between 0 and 7 goals
                    S[p][e][d] = random.randint(0,7)

    #  Count points for each team
    for p in range(6):
        # Day 1
        P = match(P,S,p,0,0,1)
        P = match(P,S,p,0,2,3)
        # Day 2
        P = match(P,S,p,1,0,2)
        P = match(P,S,p,1,1,3)
        # Day 3
        P = match(P,S,p,2,0,3)
        P = match(P,S,p,2,1,2)

    Pf = flatten(P)
    rank = sorted(range(24), key=lambda k: Pf[k])
    for r in rank[8:24]:
        qualified[r] += 1

rank_ = sorted(range(24), key=lambda k: qualified[k])

print("Probability of team being qualified ({})".format(datetime.date.today()))
for i in rank_[::-1]:
    print("{} : {:.1f} %".format(Gf[i], qualified[i] / n * 100))