# Versao do Python: 3.10.12

from Trie import Trie

tr = Trie()
#print(*tr.raiz.ref)
for n in tr.raiz.ref:
    print("chave:" + n.chave)
print("raiz:" + tr.raiz.chave)

# def comando(cmd: str = ""):
#     if cmd == "":
#         return

#     return {
#         "p": "fazer",
#         "c": "fazer",
#         "f": "fazer",
#         "e": "fazer",
#         }[cmd]
