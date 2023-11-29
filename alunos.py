#Sistema com Dicionário em Python
#apresentando ao usuário
print('\n\t\t\t  --  SISTEMA ESCOLAR SIMPLES  --')

#criando um dicionário para os dados a serem inseridos
cadastro = {}

#entradas
nome = str(input('Nome do aluno: '))
nota = float(input('Nota: '))
curso = str(input('Curso: '))
matricula = str(input('Aluno ativo? (s/n): '))

'''
#criando o tipo booleano (TENTATIVA FRUSTRADA!)
s = True
n = False
matricula = str(input('Matrícula ativa? (s/n): '))
'''

'''
#TESTE COM BOOLEANO, SEM SUCESSO!
print(s)
print(n)
print(matricula)    #SEMPRE "TRUE"!
'''

#adicionando os dados inseridos ao dicionário
cadastro[nome] = {'nota': nota, 'curso': curso, 'matricula': matricula}

#apresentação sem booleano
if matricula == 'n':
    print('O aluno: ' + nome + ' esta inativo na turma ' + curso + '.')
elif matricula == 's':
    print('O aluno: ' + nome + ' esta ativo na turma ' + curso + ', obtendo uma nota ' f'{nota}' '.')
else:
    print('Valor utilizado no Matrícula inválido! Tente novamente.')

'''
#condicional simples para apresentação dos dados (TENTATIVA FRUSTRADA!)
if matricula == False:
    print('O aluno: ' + nome + ' esta inativo na turma ' + curso + '.')
else:
    print('O aluno: ' + nome + ' esta ativo na turma ' + curso + ', obtendo uma nota ' f'{nota}' '.')
'''

