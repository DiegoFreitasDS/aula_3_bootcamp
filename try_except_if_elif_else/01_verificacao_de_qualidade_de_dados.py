### Exercício 

# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

quantidade = int(input("Digite a quantidade: \n"))
preço = int(input("Digite o preço: \n"))

if quantidade > 0 and preço > 0:
    print("Dados válidos")

else:
    print("Dados inválidos")
