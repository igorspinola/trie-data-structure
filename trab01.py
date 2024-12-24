# Versao do Python: 3.10.12

from Trie import Trie

tr: Trie = Trie()
#print(*tr.raiz.ref)
#for n in tr.raiz.ref:
#    print("chave:" + n.chave)
#print("raiz:" + tr.raiz.chave)

entrada: str = input()

while entrada != 'e':

    if entrada == 'i':
        arg = input()
        print(tr.insere(arg))
    elif entrada == 'c':
        pass
    elif entrada == 'f':
        pass
    elif entrada == 'p':
        pass
    else:
        pass

    entrada = input()
