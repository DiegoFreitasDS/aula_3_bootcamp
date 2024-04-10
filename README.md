# aula_3_bootcamp


O **try** permite testar um bloco de código em busca de erros.

O **except** permite lidar com o erro.

O **else** permite executar código quando não há erro.

O **finally** permite executar código, independentemente do resultado dos blocos try e except.


## Manipulação de exceção

Quando ocorre um erro, ou exceção como o chamamos, o Python normalmente irá parar e gerar uma mensagem de erro.

Essas exceções podem ser tratadas usando a tryinstrução:

````

try:
  print(x)
except:
  print("An exception occurred")
  
````