# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos_linkedin = ['Python', 'JavaScript', 'Data Science', 'Machine Learning', 'Web Development']
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso1 = 'Python'
curso2 = 'JavaScript'
curso3 = 'Data Science'
curso4 = 'Maquiagem'
curso5 = 'Web Development'
# 3. Crie um dicionário vazio para armazenar a nota do curso
notas_cursos = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
for curso in [curso1, curso2, curso3, curso4, curso5]:
    if curso in cursos_linkedin:
        print(f'O curso {curso} está na lista de cursos do LinkedIn Learning.')
        nota = float(input(f'Por favor, avalie o curso {curso} com uma nota de 0 a 5: '))
        notas_cursos[curso] = nota
    else:
        print(f'O curso {curso} não está na lista de cursos do LinkedIn Learning.')
# 5. Se o curso estiver na lista, solicite uma nota para avaliação

# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
print("Notas dos cursos avaliados:", notas_cursos)
