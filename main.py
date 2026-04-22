import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
tipos = ['1 - municipal',
         '2 - estadual',
         '3 - particular'
         ]

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            codigo_inep TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            nome TEXT,
            tipo TEXT,
            cidade TEXT,
            estado TEXT
               )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               email TEXT UNIQUE NOT NULL,
               senha TEXT NOT NULL,
               nome TEXT,
               idade TEXT
               )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               titulo TEXT NOT NULL,
               autor TEXT
               )
""")

def cadastrar_user():
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')

    cursor.execute("INSERT INTO usuarios(email, senha, nome, idade) VALUES(?, ?, ?, ?);",
                   (email, senha, nome, idade))


def emprestar_livros():
    cursor.execute("""SELECT * FROM livros""")
    livros = cursor.fetchall()

    print(livros)

def login_usuario():
    nome = input("Nome: ")
    email = input("Digite email: ")
    senha = input("Senha: ")
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND email = ? AND senha = ?;",
                   (nome, email, senha))
    validar_usuario = cursor.fetchone()

    if validar_usuario:
        print(f"Bem-vindo {nome}")
        print()
        print("1 - Emprestar livro")
        opcoes = input('Select: ')
        if opcoes == '1':
            print("Deu bão")
        else:
            print("Deu bão também")

def administrador():
    codigo_inep = input("Digite o código INEP da instituição: ")
    senha = input("Senha: ")
    cursor.execute("SELECT * FROM admin WHERE codigo_inep = ? AND senha = ?;",
                   (codigo_inep, senha))
    
    validar_adm = cursor.fetchone()
    
    if validar_adm:
        print(f"Bem vindo {validar_adm[0]}!")
        print()
        print('1 - acompanhar item')
        print('2 - adicionar item')
        print('3 - deletar item')
        opcoes = input('Select: ')
        if opcoes == '1':
            print(emprestar_livros())
        elif opcoes == '2':
            print(emprestar_livros())
        elif opcoes == '3':
            print(emprestar_livros)
        else:
            print("opção inválida")
    else:
        print("login inválido")

print('1 - administrador 2 - usuario')
escolha = input('Select: ')
if escolha == '1':
    administrador()
elif escolha == '2':
    print('1 - cadastro, 2 - login')
    selecao = input(': ')
    if selecao == '1':
        cadastrar_user()
        print('Usuário cadastrado com sucesso!')
        login_usuario()
    elif selecao == '2':
        login_usuario()

conn.commit()

