import random
from src.sorts.bubblesort import Bubblesort

def main():
    # gera uma lista de dados de teste
    dados = [random.randint(0, 10000) for _ in range(1000)]

    algoritmos = [
        Bubblesort(),
        # Insertionsort(),
        # Selectionsort(),
        # ...
    ]

    for alg in algoritmos:
        copia = dados.copy()  # cada algoritmo ordena sua própria cópia
        alg.ordenar(copia)
        print(alg)


if __name__ == "__main__":
    main()