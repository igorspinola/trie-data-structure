from typing import List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz = No()
        i: int = 97
        while i < 123:
           self.raiz.ref.append(No(chr(i)))
           i += 1

    def insere(self, palavra: str) -> List[str]:
        # early return caso já esteja na trie
        atual = self.raiz
        for letra in palavra:
            if letra in atual.ref.chave:
                continue

            i: int = 0
            while i < 27:
                atual = atual.ref[i]
                if atual.chave == letra:
                    break
                i += 1
        return [""]
