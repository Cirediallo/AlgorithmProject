import algorithms.LSA as LSA
import algorithms.LPT as LPT
import algorithms.RMA as RMA

testing_values = [i for i in range(
    1, 10, 1)] + [i for i in range(10, 59, 5)] + [i for i in range(60, 99, 10)] + [i for i in range(100, 201, 20)] + [300]

with open("test_results.txt", "w") as f:
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

        print(f'Borne inferieure "maximum" = {borne_inferieure_maximum}')
        print(f'Borne inferieure "moyenne" = {borne_inferieure_moyenne}')
        #print(f'B = {B}\n')

        print(f'Resultat LSA = {LSA_result}')
        print(f'ratio LSA = {(LSA_result / B):.2f}\n')
        print(f'Resultat LPT = {LPT_result}')
        print(f'ratio LPT = {(LPT_result / B):.2f}\n')
        print(f'Resultat RMA = {RMA_result}')
        print(f'ratio RMA = {(RMA_result / B):.2f}\n')

        f.write(
            f'{p}\t{(LSA_result / B):.2f}\t{(LPT_result / B):.2f}\t{(RMA_result / B):.2f}\n')
