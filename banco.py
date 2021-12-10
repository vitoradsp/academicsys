import sqlite3

def conectar():
    banco = sqlite3.connect('banco.db')
    return banco

def criar_tabela_usuario():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(usuario TEXT, senha TEXT, cargo TEXT, excluida BOOLEAN)')
    banco.commit()
    banco.close()

def criar_tabela_nota_aluno():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS notasaluno (nota1 TEXT, nota2 TEXT , nota3 TEXT, materia TEXT, turma TEXT, excluida BOOLEAN, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_alunos():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (nome TEXT, turma TEXT, cpf INTEGER, falta INTEGER, curso TEXT, datadenascimento TEXT, excluida BOOLEAN, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_professores():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS professores (nome TEXT, cpf INTEGER, turma TEXT, materia TEXT, excluida BOOLEAN, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()
    
def inserir_usuario(usuario, senha, cargo, excluida):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO usuarios VALUES('{usuario}', '{senha}', '{cargo}', {excluida})")
    banco.commit()
    banco.close()

def inserir_notas_aluno(nota1, nota2, nota3, materia, turma, excluida, usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO notasaluno VALUES('{nota1}', '{nota2}', '{nota3}', '{materia}', '{turma}', {excluida}, {usuario_id})")
    banco.commit()
    banco.close()

def editar_notas_aluno(nota1, nota2, nota3, materia, turma, excluida, usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE notasaluno SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', materia='{materia}', turma='{turma}', excluida={excluida} WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_falta_aluno(faltas, usuario_id):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE alunos SET falta={faltas} WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def inserir_professor(nome, cpf, turma, materia, excluida, usuario_id):
    criar_tabela_professores()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO professores VALUES("{nome}", {cpf}, "{turma}", "{materia}", {excluida}, {usuario_id})')
    banco.commit()
    banco.close()

def inserir_aluno(nome, turma, cpf, falta, curso, datadenascimento, excluida, usuario_id):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO alunos VALUES('{nome}', '{turma}', {cpf}, {falta}, '{curso}' , '{datadenascimento}', {excluida}, {usuario_id})")
    banco.commit()
    banco.close()

def buscar_usuario(usuario):
    criar_tabela_usuario()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid, * FROM usuarios WHERE usuario='{usuario}'")
    return cursor.fetchone()

def buscar_notas(usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM notasaluno WHERE usuario_id={usuario_id}")
    return cursor.fetchall()

def todos_alunos_geral():
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM alunos")
    return cursor.fetchall()

def buscar_notas_por_materia_conj(materia):
    criar_tabela_nota_aluno()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, n.materia FROM notasaluno n JOIN alunos a ON a.usuario_id = n.usuario_id AND a.turma = n.turma WHERE n.materia='{materia}'")
    return cursor.fetchall()

def buscar_nota_por_materia(materia, usuario_id):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM notasaluno WHERE materia='{materia}' AND usuario_id={usuario_id}")
    return cursor.fetchone()

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

def buscar_todos_alunos_com_nota():
    criar_tabela_nota_aluno()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, n.materia FROM notasaluno n JOIN alunos a ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_notas_da_materia_por_turma(materia, turma):
    criar_tabela_nota_aluno()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, n.materia FROM notasaluno n JOIN alunos a ON a.usuario_id = n.usuario_id JOIN professores p ON p.materia = n.materia WHERE p.materia='{materia}' AND a.turma='{turma}'")
    return cursor.fetchall()

def deletar_aluno_por_cpf(cpf):
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE alunos set excluida={True} WHERE cpf={cpf}")
    banco.commit()
    banco.close()

def deletar_professor_por_cpf(cpf):
    criar_tabela_professores()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM professor WHERE cpf='{cpf}'")
    banco.commit()
    banco.close()   



if __name__ == "__main__":
    criar_tabela_usuario()
    criar_tabela_nota_aluno()
    inserir_usuario("root", "123", "Secretaria", False)    
