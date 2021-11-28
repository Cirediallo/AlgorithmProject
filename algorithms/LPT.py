def run(D, M):
    """
    trie d’abord les taches par ordre decroissant. Ensuite,
    LPT affecte chaque tache, dans l’ordre du tri, a la 
    premiere machine disponible
    """
    D = sorted(D, reverse=True)

    for task in D:
        first_available_machine = M.index(min(M))
        M[first_available_machine] += task

    return max(M)
