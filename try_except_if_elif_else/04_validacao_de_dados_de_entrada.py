### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Digite a idade do registro: \n"))
email = str(input("Digite o email do registro: \n"))


if not 18 <= idade <= 65:
    print("Idade fora dos parâmetros")
elif "@" not in email or "." not in email:
    print("Email inválido")
else:
    print(f"Idade {idade} e {email} serão processada")