import random


def run(D, M):
    """
    pour chaque tache dans l’ordre initialement fourni,
    determine au hasard quelle machine va l’executer
    """
    for task in D:
        random_machine = random.randint(0, len(M) - 1)
        M[random_machine] += task

    return max(M)
