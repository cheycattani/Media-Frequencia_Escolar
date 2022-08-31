# Peça ao usuário as seguintes informações sobre um aluno:
# Nome, Nota Prova 1, Nota prova 2 e Total de faltas.
# Considere que foram dadas 20 aulas e que para passar o aluno precisa de pelo menos 70% de presença e média 6 ou mais.
# Ao final imprima: Nome do aluno, média, percentual de presença (assiduidade) e resultado
# (reprovado por faltas e por média, reprovado por faltas, reprovado por média ou aprovado)

nome_aluno = input('Digite seu nome: ')
prova1 = float(input('Digite a nota da prova 1: '))
prova2 = float(input('Digite a nota da prova 2: '))
media = (prova1 + prova2) / 2

faltas = int(input('Digite o total de faltas: '))
aulas = 20
frequencia = (((aulas - faltas) / aulas) * 100)

if frequencia >= 70 and media >= 6:
    resultado = 'Parabéns, aluno aprovado!'
elif frequencia < 70 and media < 6:
    resultado = 'Aluno reprovado por falta e nota!'
elif frequencia < 70 and media >= 6:
    resultado = 'Aluno reprovado por falta!'
else:
    resultado = 'Aluno reprovado por nota!'

print('Nome:', nome_aluno)
print('Média:', media)
print('Frequência:',frequencia, '%')
print('Resultado:', resultado)
