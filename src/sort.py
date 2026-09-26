from abc import ABC, abstractmethod
import time

class Sort(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.comparacoes = 0
        self.trocas = 0
        self.tempo = 0

    def ordenar(self,data):
        self.comparacoes = 0
        self.trocas = 0
        inicio = time.time()
        self.sort(data)
        self.tempo = time.time() - inicio
        
        return len(data), self.tempo
    
    @abstractmethod
    def sort(self, data):
        pass

    def __str__(self):
        return (f"{self.nome:<15} | comparações: {self.comparacoes:>8} | "
            f"trocas: {self.trocas:>8} | tempo: {self.tempo:.6f}s")

    def __repr__(self):
        return (f"Sort(nome={self.nome!r}, comparacoes={self.comparacoes}, "
            f"trocas={self.trocas}, tempo={self.tempo})")

    def menor(self, a, b):
        # Retorna a < b e conta UMA comparação.
        self.comparacoes += 1
        return a < b

    def menor_ou_igual(self, a, b):
        # Retorna a <= b e conta UMA comparação (útil para manter estabilidade).
        self.comparacoes += 1
        return a <= b

    def trocar(self, v, i, j):
        # Troca v[i] e v[j] e conta UMA troca.
        v[i], v[j] = v[j], v[i]
        self.trocas += 1

    def escrever(self, v, i, valor):
        # Escreve valor em v[i] e conta UMA movimentação.
        v[i] = valor
        self.trocas += 1