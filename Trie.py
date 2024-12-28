from typing import Dict, List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        self.contador: Dict[str, int] = {}

        # i: int = 97
        # while i < 123:
        #    self.raiz.ref.append(No(chr(i)))
        #    i += 1

    def insere(self, palavra: str) -> str:
        output: str = "palavra ja existente: " + palavra
        atual: No = self.raiz
        j: int = 0
        for le in palavra:
            # if len(atual.ref) != 0 and atual.ref[-1] == "*":
            #     atual.ref.pop()
            # print("tamanho:")
            # print(len(atual.ref))
            if len(atual.ref) == 0 or len(atual.ref) == 1:
                for i in range(27):
                    atual.ref.append(No(""))
            # print("tamanho novo:")
            # print(len(atual.ref))
            # if len(atual.ref) == 1 and atual.ref[0].chave == "*":
            #     atual.ref.pop()
            #     for i in range(26):
            #         atual.ref.append(No(""))
            #     atual.ref.append(No("*"))
            # if j == len(palavra) - 1:
            #     indice = ord(le) - ord('a') + 1
            #     # if j == len(atual.ref) - 1 entao indice = ord(le) - ord(a) + 1
            #     if atual.ref[indice].chave == "":
            #         atual.ref[indice] = No(le)
            #         output = "palavra inserida: " + palavra
            #         if not self.contador.get(palavra):
            #             self.contador[palavra] = 0
            #     atual = atual.ref[indice]
            # else:
            #     indice = ord(le) - ord('a')
            #     # if j == len(atual.ref) - 1 entao indice = ord(le) - ord(a) + 1
            #     if atual.ref[indice].chave == "":
            #         atual.ref[indice] = No(le)
            #         output = "palavra inserida: " + palavra
            #         if not self.contador.get(palavra):
            #             self.contador[palavra] = 0
            #     atual = atual.ref[indice]

            indice = ord(le) - ord('a') + 1
            # if j == len(atual.ref) - 1 entao indice = ord(le) - ord(a) + 1
            if atual.ref[indice].chave == "":
                atual.ref[indice] = No(le)
                output = "palavra inserida: " + palavra
                if not self.contador.get(palavra):
                    self.contador[palavra] = 0
            atual = atual.ref[indice]
            if j == len(palavra) - 1:
                # o caractere de final de palavra fica no indice 26 (atual.ref[26])
                #atual.ref.insert(0, No("*"))
                if len(atual.ref) == 0:
                    atual.ref.append(No("*"))
                atual.ref[0] = No("*")
                # print("array ref:")
                # for e in atual.ref:
                #     if e.chave != "":
                #         print(e.chave)
            j += 1
        return output

    def consulta(self, palavra: str) -> str:

        output: str = ""
        atual: No = self.raiz
        j: int = 0

        for le in palavra:
            indice: int = ord(le) - ord('a') + 1
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

    def imprimir(self, no: No, ehRaiz: bool = True) -> None :
        if no.chave == "*":
            print("letra: *")
            return
        elif ehRaiz:
            output: str = "letra: " + "raiz" + " -"
            if len(no.ref) == 0:
                print("trie vazia")
                return
            for le in no.ref:
                if le.chave == "":
                    continue
                # if len(no.ref) == 27:
                #     if le.chave != "":
                #         output += " *"
                #         output += " " + le.chave
                else:
                    if le.chave != "":
                        output += " " + le.chave
            print(output)
        else:
            output: str = "letra: " + no.chave + " -"
            # if ultimoElemento.chave == "*" or len(no.ref) == 0:
            #         output += " *"
            # if no.ref[0].chave == "*":
            #         output += " *"
            for le in no.ref:
                if le.chave == "":
                    continue
                # if len(no.ref) == 27:
                #     if le.chave != "":
                #         output += " *"
                #         output += " " + le.chave
                if le.chave != "":
                    output += " " + le.chave
                # if no.ref[len(no.ref) - 1] == "*":
                #     if le.chave != "":
                #         output += " *"
                #         output += " " + le.chave
                # else:
                #     if le.chave != "":
                #         output += " " + le.chave
            print(output)

        for filho in no.ref:
            if filho.chave != "":
                self.imprimir(filho, False)

    def imprimir_arvore(self) -> None:
        self.imprimir(self.raiz)

    def imprimir_(self) -> None:
        atual: No = self.raiz
        atual = atual.ref[0]
        output: str = ""
        output = "letra: raiz " + "-"
        for filho in self.raiz.ref:
            output += " " + filho.chave
        print(output)
        for filho in self.raiz.ref:
            if atual.chave == "*":
                pass
            else:
                output = "letra: "
            for le in atual.ref:
                if le.chave != "":
                    output += le.chave
            print(output)
            atual = atual.ref[0]
