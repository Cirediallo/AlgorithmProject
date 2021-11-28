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

LSA_results = LSA.run(D, M)
LPT_results = LPT.run(D, M)
RMA_results = RMA.run(D, M)

print(f'T_lsa = {LSA_results}')
print(f'T_lpt = {LPT_results}')
print(f'T_rma = {RMA_results}')
