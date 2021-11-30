import sys
import algorithms.LSA as LSA
import algorithms.LPT as LPT
import algorithms.RMA as RMA
import random
from statistics import mean

input_mode = int(input("Choose an input mode:\n1 - Ip\n2 - Ir\n\n"))

D = []
M = []

# Ip input mode
if input_mode == 1:
    p = int(input("Enter a value for p: "))

    D = [1 for i in range(4 * p)] + \
        [2 for i in range(2 * p * (p - 1))] + [2 * p]

    M = [0 for i in range(2 * p)]

    LSA_result = LSA.run(D, M.copy())
    LPT_result = LPT.run(D, M.copy())
    RMA_result = RMA.run(D, M.copy())

    borne_inferieure_moyenne = sum(D) / len(M)
    borne_inferieure_maximum = max(D)

    #print(f'D: {D}\n')
    #print(f'M: {M}\n')
    B = max(borne_inferieure_moyenne, borne_inferieure_maximum)

    print(f'Borne inferieure "maximum" = {borne_inferieure_maximum}')
    print(f'Borne inferieure "moyenne" = {borne_inferieure_moyenne}')
    #print(f'B = {B}\n')

    print(f'Resultat LSA = {LSA_result}')
    print(f'ratio LSA = {(LSA_result / B):.2f}\n')
    print(f'Resultat LPT = {LPT_result}')
    print(f'ratio LPT = {(LPT_result / B):.2f}\n')
    print(f'Resultat RMA = {RMA_result}')
    print(f'ratio RMA = {(RMA_result / B):.2f}\n')


elif input_mode == 2:
    m = int(input("Enter a value for m: "))
    n = int(input("Enter a value for n: "))
    k = int(input("Enter a value for k: "))
    d_min = int(input("Enter a value for d_min: "))
    d_max = int(input("Enter a value for d_max: "))

    LSA_mean_ratio = []
    LPT_mean_ratio = []
    RMA_mean_ratio = []

    for i in range(0, k):
        M = [0 for i in range(m)]
        D = [random.randint(d_min, d_max) for i in range(n)]

        borne_inferieure_moyenne = sum(D) / len(M)
        borne_inferieure_maximum = max(D)

        B = max(borne_inferieure_moyenne, borne_inferieure_maximum)

        LSA_mean_ratio.append(LSA.run(D, M.copy()) / B)
        LPT_mean_ratio.append(LPT.run(D, M.copy()) / B)
        RMA_mean_ratio.append(RMA.run(D, M.copy()) / B)

    print(f'ratio moyen LSA = {mean(LSA_mean_ratio):.2f}')
    print(f'ratio moyen LPT = {mean(LPT_mean_ratio):.2f}')
    print(f'ratio moyen RMA = {mean(RMA_mean_ratio):.2f}')

else:
    print("Invalid input mode")
    sys.exit()
