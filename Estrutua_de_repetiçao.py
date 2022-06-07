print("Exemplo 01 de While - Enquanto\n")
senha = "54321"
leitura = " "
while (leitura != senha):
  leitura = input("Digite a senha: ")
  if leitura == senha:
    print ('Acesso liberado')
  else:
    print ('Senha incorreta. Tente novamente')
#---------------------------------------------------#
print("\nExemplo 02 de While - Enquanto\n")
contador = 0
somador = 0
while contador < 5:
  contador = contador + 1
  valor = float(input('Digite o '+str(contador)+'º valor: '))
  somador = somador + valor
print('Soma = ',somador)
#str -> retorna a váriavel contador na forma de string.

#---------------------------------------------------#
print("\nExemplo 01 de 'For'. Encontrar a soma S = 1+4+7+10+13+16+19\n")
s = 0
for x in range(1,20,3):
  s += x
print('Soma = ',s)
#A função range() define um intervalo de valores inteiros.
#---------------------------------------------------#
print("\nExemplo 02 de 'For'. As notas de um aluno estão armazenadas em uma lista. Calcular a média dessas notas.")
Lista_notas = [3.4,6.6,8,9,10,9.5,8.8,4.3]
soma = 0
for nota in Lista_notas:
  soma += nota
média = soma/len(Lista_notas)
print('Média = %2.f'%média)
