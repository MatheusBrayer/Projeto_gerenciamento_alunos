import sqlite3

def conectar_db():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR (100) NOT NULL,
                email VARCHAR (100),
                telefone VARCHAR (20) NOT NULL
                )
    ''')
    conn.commit()
    conn.close()

def cadastrar_aluno(nome, email, telefone):
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO alunos (nome, email, telefone)
        VALUES (?,?,?)''',
        (nome,email,telefone))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM alunos
    ''')
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def excluir_aluno(id):
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alunos WHERE id=?', (id,))
    conn.commit()
    conn.close()

def atualizar_aluno(id, nome, email, telefone):
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE alunos 
        SET nome = ?, email = ?, telefone = ?
        WHERE id = ?''', (nome, email, telefone, id))
    conn.commit()
    conn.close()


if __name__=="__main__":
    conectar_db()
    print('Banco de dados criado com sucesso!')