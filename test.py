import algorithms.LSA as LSA
import algorithms.LPT as LPT
import algorithms.RMA as RMA

import itertools
import random
from statistics import mean

testing_values = [i for i in range(
    1, 10, 1)] + [i for i in range(10, 59, 5)] + [i for i in range(60, 99, 10)] + [i for i in range(100, 201, 20)] + [300]

with open("results/ip_test_results.txt", "w") as f:
    # Test pour Ip
    for p in testing_values:
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
        """
        print(f'Borne inferieure "maximum" = {borne_inferieure_maximum}')
        print(f'Borne inferieure "moyenne" = {borne_inferieure_moyenne}')
        #print(f'B = {B}\n')

        print(f'Resultat LSA = {LSA_result}')
        print(f'ratio LSA = {(LSA_result / B):.2f}\n')
        print(f'Resultat LPT = {LPT_result}')
        print(f'ratio LPT = {(LPT_result / B):.2f}\n')
        print(f'Resultat RMA = {RMA_result}')
        print(f'ratio RMA = {(RMA_result / B):.2f}\n')
        """
        f.write(
            f'{p}\t{(LSA_result / B):.2f}\t{(LPT_result / B):.2f}\t{(RMA_result / B):.2f}\n')


tests_k = [30]
tests_n = [10, 50, 250, 500]
tests_m = [2, 5, 25, 50]
tests_d_max = [10, 100]

with open('results/ir_test_results.txt', 'w') as f:
    for params in list(itertools.product(*[tests_k, tests_n, tests_m, tests_d_max])):
        # print(params)
        LSA_mean_ratio = []
        LPT_mean_ratio = []
        RMA_mean_ratio = []

        k = params[0]
        n = params[1]
        m = params[2]
        d_max = params[3]
        d_min = 0

        for i in range(0, k):
            M = [0 for i in range(m)]
            D = [random.randint(d_min, d_max) for i in range(n)]

            borne_inferieure_moyenne = sum(D) / len(M)
            borne_inferieure_maximum = max(D)

            B = max(borne_inferieure_moyenne, borne_inferieure_maximum)

            LSA_mean_ratio.append(LSA.run(D, M.copy()) / B)
            LPT_mean_ratio.append(LPT.run(D, M.copy()) / B)
            RMA_mean_ratio.append(RMA.run(D, M.copy()) / B)

        f.write(
            f'[k={k}, n={n}, m={m}, d_min={d_min}, d_max={d_max}]\tRatioLSA={mean(LSA_mean_ratio):.2f}\tRatioLPT={mean(LPT_mean_ratio):.2f}\tRatioRMA={mean(RMA_mean_ratio):.2f}\n')
