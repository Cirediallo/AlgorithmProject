input_mode = int(input("Choose an input mode:\n1 - Ip\n2 - Ir\n\n"))

# Ip input mode
if input_mode == 1:
    p = int(input("Enter a value for p: "))

    instance = [1 for p in range(4 * p)] + \
        [2 for p in range(2 * p * (p - 1))] + [2 * p]
    print(instance)
elif input_mode == 2:
    print('XD')
else:
    print("Invalid input mode")
