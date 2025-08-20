#Tipos de dados que temos em Python a serem estudados: List, Tupla, Set, DIC...

#Condição/tomada de decisão (obs: max de 3 condições por if, não pode ter muitos ifs no cod)
i = 1 
f = 2
if i > f:
    print(f"O número {i} é maior que {f}" )
else:
    print(f"O número {f} é maior que {i}" )

print("i")

#função  q,f não são variáveis, são PARAMETROS       --Sem o *return* é uma procedimento
def somar(q,f):
    soma = q + f
    return soma

somar(10,21)

print(somar(10,21))

#Matriz
i = 100 #Escalar
i = [10,20] #Vetor
i = [[10,20], [30,40]] #Matriz

#Repetições  Palavras Reservadas= break(Para todo o while), continue (para apenas uma condição interna)
d = 0
while(d<5): 
    d = d + 1 # or d += 1
    print(d)

for letra in "senac":
    if (v := letra) == "s":
        print("pega esse ssssss")
    else:
        print(v)