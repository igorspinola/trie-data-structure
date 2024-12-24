from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        i: int = 97

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
            atual = atual.ref[indice]

        return output
