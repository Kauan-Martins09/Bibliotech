import sqlite3
import deletar
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            inst TEXT NOT NULL,
            senha TEXT NOT NULl
               )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               email TEXT NOT NULL,
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
    email = input("EMAIL: ")
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
    inst = input("Instituição: ")
    senha = input("Senha: ")
    cursor.execute("SELECT * FROM admin WHERE inst = ? AND senha = ?;",
                   (inst, senha))
    
    validar_adm = cursor.fetchone()

    if validar_adm:
        print(f"Bem vindo {inst}!")
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

