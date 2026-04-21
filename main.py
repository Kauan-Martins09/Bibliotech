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
               cpf TEXT UNIQUE NOT NULL,
               senha TEXT NOT NULL,
               nome TEXT,
               idade TEXT
               )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               titulo TEXT NOT NULL,
               autor TEXT,
               data_emprestimo TEXT NOT NULL,
               data_devolução TEXT
               )
""")

def usuario():
    nome = input("Nome: ")
    cpf = input("Digite CPF: ")
    senha = input("Senha: ")
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND cpf = ? AND senha = ?;",
                   (nome, cpf, senha))
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
            print("FUNCIONA")
        elif opcoes == '2':
            print("FUNCIONA")
        elif opcoes == '3':
            print("FUNCIONA")
        else:
            print("opção inválida")
    else:
        print("login inválido")

print('1 - administrador 2 - usuario')
escolha = input('Select: ')
if escolha == '1':
    administrador()
elif escolha == '2':
    usuario()

conn.commit()

