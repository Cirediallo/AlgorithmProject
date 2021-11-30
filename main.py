import sys
import algorithms.LSA as LSA
import algorithms.LPT as LPT
import algorithms.RMA as RMA

input_mode = int(input("Choose an input mode:\n1 - Ip\n2 - Ir\n\n"))

D = []
M = []

# Ip input mode
if input_mode == 1:
    p = int(input("Enter a value for p: "))

    D = [1 for i in range(4 * p)] + \
        [2 for i in range(2 * p * (p - 1))] + [2 * p]

    M = [0 for i in range(2 * p)]

elif input_mode == 2:
    print('XD')
else:
    print("Invalid input mode")
    sys.exit()

print(f'D: {D}\n')
print(f'M: {M}\n')

LSA_result = LSA.run(D, M.copy())
LPT_result = LPT.run(D, M.copy())
RMA_result = RMA.run(D, M.copy())

borne_inferieure_moyenne = sum(D) / len(M)
borne_inferieure_maximum = max(D)

B = max(borne_inferieure_moyenne, borne_inferieure_maximum)

print(f'Borne inferieure "maximum" = {borne_inferieure_maximum}')
print(f'Borne inferieure "moyenne" = {borne_inferieure_moyenne}')
print(f'B = {B}\n')

print(f'Resultat LSA = {LSA_result}')
print(f'ratio LSA = {(LSA_result / B):.2f}\n')
print(f'Resultat LPT = {LPT_result}')
print(f'ratio LPT = {(LPT_result / B):.2f}\n')
print(f'Resultat RMA = {RMA_result}')
print(f'ratio RMA = {(RMA_result / B):.2f}\n')
