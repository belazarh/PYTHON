# Execício 1

texto = "O senac é legal".lower()

vogal = ['a','e','i','o','u']
vogais_acentuadas = "áàãâäéèêëíìîïóòõôöúùûü"
contador = 0
for i in texto:
    if i in vogal or i in vogais_acentuadas:
        contador += 1

print (contador)

#Exercício 2
texto = "O senac é legal".split(" ")
qtd = 0
for i in texto:
    print(i)
    qtd +=1
print (qtd)