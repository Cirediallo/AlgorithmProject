import sys
import algorithms.LSA as LSA
import algorithms.LPT as LPT
import algorithms.RMA as RMA
import random
from statistics import mean

input_mode = int(input(
    "Choisissez un mode de génération d'instance:\n1 - Mode Ip\n2 - Mode Ir\n\n"))

D = []
M = []

# Ip input mode
if input_mode == 1:
    p = int(input("Entrez la valeur du paramètre p: "))

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

    print(f'Borne inférieure "maximum" = {borne_inferieure_maximum}')
    print(f'Borne inférieure "moyenne" = {borne_inferieure_moyenne}\n')
    #print(f'B = {B}\n')

    print(f'Résultat LSA = {LSA_result}')
    print(f'ratio LSA = {(LSA_result / B):.2f}\n')
    print(f'Résultat LPT = {LPT_result}')
    print(f'ratio LPT = {(LPT_result / B):.2f}\n')
    print(f'Résultat RMA = {RMA_result}')
    print(f'ratio RMA = {(RMA_result / B):.2f}\n')


elif input_mode == 2:
    m = int(input("Entrez la valeur du paramètre m: "))
    n = int(input("Entrez la valeur du paramètre n: "))
    k = int(input("Entrez la valeur du paramètre k: "))
    d_min = int(input("Entrez la valeur du paramètre d_min: "))
    d_max = int(input("Entrez la valeur du paramètre d_max: "))

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
