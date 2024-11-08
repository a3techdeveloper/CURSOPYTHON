#Variáveis - Locais reservados na memória ram onde guardamos algum dado
canal     = 'Curso de Python'
aluno     = "Anderson Henrique"
framework = 'Django 3.0'

print(canal+', '+aluno+', '+framework)

#Funções - pedaços de código que executam um bloco de instruções
#Criando a função - imprime uma variavel global
def cr():
    print(canal)

#Chamar a função
cr()

#Imprime uma variavel local
def cn():
    global linguagem
    linguagem = 'Python'

#Chama a função
cn()
print(linguagem)
