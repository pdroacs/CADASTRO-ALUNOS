from db.conexao import conectar


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            curso TEXT
        )
    ''')
    conn.commit()
    conn.close()


def inserir_aluno(nome, idade, curso):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)', (nome, idade, curso))
    conn.commit()
    conn.close()


def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return alunos


def atualizar_aluno(id, nome, idade, curso):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE alunos
        SET nome = ?, idade = ?, curso = ?
        WHERE id = ?
    ''', (nome, idade, curso, id))
    conn.commit()
    conn.close()


def remover_aluno(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
