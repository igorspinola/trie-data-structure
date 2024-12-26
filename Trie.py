from typing import Dict, List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        i: int = 97
        self.contador: Dict[str, int] = {}

        while i < 123:
           self.raiz.ref.append(No(chr(i)))
           i += 1

    def insere(self, palavra: str) -> str:
        output: str = "palavra ja existente: " + palavra
        atual: No = self.raiz

        for le in palavra:
            if len(atual.ref) == 0:
                for i in range(26):
                    atual.ref.append(No(""))
            indice = ord(le) - ord('a')
            if atual.ref[indice].chave == "":
                atual.ref[indice] = No(le)
                output = "palavra inserida: " + palavra
                if not self.contador.get(palavra):
                    self.contador[palavra] = 0
            atual = atual.ref[indice]
        return output

    def consulta(self, palavra: str) -> str:

        output: str = ""
        atual: No = self.raiz
        j: int = 0

        for le in palavra:
            indice: int = ord(le) - ord('a')
            if len(atual.ref) == 0 and j == len(palavra) - 1:
                if not self.contador.get(palavra):
                    self.contador[palavra] = 0
                self.contador[palavra] += 1
                output = "palavra existente: " + palavra + " " + str(self.contador[palavra])
                return output
            if len(atual.ref) == 0 and j != len(palavra)- 1:
                output = "palavra inexistente: " + palavra
                return output
            if atual.ref[indice].chave == "":
                output = "palavra inexistente: " + palavra
                return output

            atual = atual.ref[indice]
            j += 1

        if not self.contador.get(palavra):
            self.contador[palavra] = 0
        self.contador[palavra] += 1
        output = "palavra existente: " + palavra + " " + str(self.contador[palavra])
        return output

    def rankear(self) -> List:
        max: int = 0
        chaves: List[str] = []
        for e in self.contador:
            valor = self.contador[e]
            if max < valor:
                max = valor
        for e in self.contador:
            if self.contador[e] == max:
                chaves.append(e)
        chaves.sort()
        return [chaves, max]
