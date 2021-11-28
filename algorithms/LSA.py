def run(D, M):
    """
    prend les taches dans l’ordre initialement fourni, et
    affecte chaque tache a la premiere machine disponible
    """
    for task in D:
        first_available_machine = M.index(min(M))
        M[first_available_machine] += task

    return max(M)
