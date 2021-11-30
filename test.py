import algorithms.LPT as LPT

D = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6]
M = [0, 0, 0, 0, 0, 0]

LPT_result = LPT.run(D, M)

borne_inferieure_moyenne = sum(D) / len(M)
borne_inferieure_maximum = max(D)
B = max(borne_inferieure_moyenne, borne_inferieure_maximum)

print(f'Borne inferieure "maximum" = {borne_inferieure_maximum}')
print(f'Borne inferieure "moyenne" = {borne_inferieure_moyenne}')
print(f'B = {B}')

print(f'Resultat LPT = {LPT_result}')
print(f'ratio LPT = {(LPT_result / B):.2f}\n')
