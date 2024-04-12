### Exercício 2: Classificação de Dados de Sensor

# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temp = int(input("Digite a temperatura: \n"))

if temp >= 18 and temp <= 26:
    print(f"\n Temperatura {temp}º normal.")
elif temp < 18:
    print(f"\n Temperatura {temp}º é baixa.")
else:
    print(f"\n Temperatura {temp}º Alta")