import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

#cursor.execute("INSERT INTO admin(inst, senha) VALUES(?, ?)",
#               ('archelau', '12345')
 #              ) 

cursor.execute("INSERT INTO usuarios(nome, email, senha) VALUES(?, ?, ?)", 
               ('kauan', 'kauanmartinsesilva@gmail.com', 'naty'))
conn.commit()