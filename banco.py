import sqlite3

def conectar():
    banco = sqlite3.connect('banco.db')
    return banco

def criar_tabela_usuario():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(usuario TEXT, senha TEXT, cargo TEXT)')
    banco.commit()
    banco.close()

def criar_tabela_falta_alunos():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS faltaalunos (faltas INTEGER, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_aluno():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS notasaluno (nota1 TEXT, nota2 TEXT , nota3 TEXT, materia TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_alunos():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (nome TEXT, turma TEXT, cpf INTEGER, curso TEXT, datadenascimento TEXT, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_professores():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS professores (nome TEXT, cpf INTEGER, turma TEXT, materia TEXT, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()
    
def inserir_usuario(usuario, senha, cargo):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO usuarios VALUES('{usuario}', '{senha}', '{cargo}')")
    banco.commit()
    banco.close()

def inserir_notas_aluno(nota1, nota2, nota3, materia, usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO notasaluno VALUES('{nota1}', '{nota2}', '{nota3}', '{materia}', {usuario_id})")
    banco.commit()
    banco.close()

def editar_notas_aluno(nota1, nota2, nota3, materia, usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE notasaluno SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', materia='{materia}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def inserir_falta_para_aluno(falta, usuario_id):
    criar_tabela_falta_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO faltaalunos VALUES({falta}, {usuario_id})")
    banco.commit()
    banco.close()

def inserir_professor(nome, cpf, turma, materia, usuario_id):
    criar_tabela_professores()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO professores VALUES("{nome}", {cpf}, "{turma}", "{materia}", {usuario_id})')
    banco.commit()
    banco.close()

def inserir_aluno(nome, turma, cpf, curso, datadenascimento, usuario_id):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO alunos VALUES('{nome}', '{turma}', {cpf}, '{curso}' , '{datadenascimento}', {usuario_id})")
    banco.commit()
    banco.close()

def buscar_usuario(usuario):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM usuarios WHERE usuario='{usuario}'")
    return cursor.fetchone()

def buscar_faltas_por_user_id(usuario_id):
    criar_tabela_falta_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM faltaalunos WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_notas(usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM notasaluno WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia(materia, usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM notasaluno WHERE materia='{materia}' AND usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_todas_notas_por_materia(materia):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM notasaluno WHERE materia='{materia}'")
    return cursor.fetchall()

def buscar_professor_user_id(usuario_id):
    criar_tabela_professores()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM professores WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_professor_por_cpf(cpf):
    criar_tabela_professores()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM professores WHERE cpf={cpf}")
    return cursor.fetchone()

def buscar_aluno_por_cpf(cpf):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM alunos WHERE cpf={cpf}")
    return cursor.fetchone()

def buscar_aluno_por_nome_e_turma(nome,turma):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM alunos WHERE nome='{nome}' AND turma='{turma}'")
    return cursor.fetchone()

def buscar_toda_turma(turma):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM alunos WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_aluno_por_id(usuario_id):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM alunos WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_alunos_mesma_turma(turma):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM alunos WHERE turma='{turma}'")
    return cursor.fetchall()

def alterar_usuario(nome, senha, cargo):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE usuarios SET nome='{nome}', senha='{senha}', adm={cargo} WHERE rowid={id}")
    banco.commit()
    banco.close()

def deletar_notas_materia(materia):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM notasaluno WHERE materia='{materia}'")
    return cursor.fetchone()

def deletar_usuario(usuario):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM produtos WHERE usuario='{usuario}'")
    banco.commit()
    banco.close()

if __name__ == "__main__":
    criar_tabela_usuario()
    inserir_usuario("123", "123", "Secretaria")    
