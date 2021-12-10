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

def criar_tabela_nota_matematica():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS matematica(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_portugues():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS portugues(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_fisica():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS fisica(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_geografia():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS geografia(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_filosofia():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS filosofia(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_historia():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS historia(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
    banco.commit()
    banco.close()

def criar_tabela_nota_biologia():     
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS biologia(nota1 TEXT, nota2 TEXT , nota3 TEXT, turma TEXT, usuario_id INTEGER , FOREIGN KEY(usuario_id) REFERENCES usuarios(id));')
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

def inserir_notas_aluno_portugues(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_portugues()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO portugues VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def inserir_notas_aluno_matematica(nota1, nota2, nota3, turma, usuario_id):
    criar_tabela_nota_matematica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO matematica VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def inserir_notas_aluno_geografia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_geografia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO geografia VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def inserir_notas_aluno_filosofia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_filosofia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO filosofia VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def inserir_notas_aluno_historia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_historia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO historia VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def inserir_notas_aluno_biologia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_biologia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO biologia VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def inserir_notas_aluno_fisica(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_fisica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO fisica VALUES('{nota1}', '{nota2}', '{nota3}', '{turma}', {usuario_id})")
    banco.commit()
    banco.close()

def editar_notas_aluno_historia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_historia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE historia SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_notas_aluno_biologia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_biologia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE biologia SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_notas_aluno_filosofia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_filosofia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE filosofia SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_notas_aluno_geografia(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_geografia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE geografia SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_notas_aluno_matematica(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_matematica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE matematica SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_notas_aluno_portugues(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_portugues()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE portugues SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
    banco.commit()
    banco.close()

def editar_notas_aluno_fisica(nota1, nota2, nota3,  turma, usuario_id):
    criar_tabela_nota_fisica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE fisica SET nota1='{nota1}', nota2='{nota2}', nota3='{nota3}', turma='{turma}' WHERE usuario_id={usuario_id}")
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
    criar_tabela_nota_historia()
    criar_tabela_nota_biologia()
    criar_tabela_nota_filosofia()
    criar_tabela_nota_geografia()
    criar_tabela_nota_matematica()
    criar_tabela_nota_portugues()
    criar_tabela_nota_fisica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM notasaluno WHERE usuario_id={usuario_id}")
    return cursor.fetchall()

def todos_alunos_geral():
    criar_tabela_nota_historia()
    criar_tabela_nota_biologia()
    criar_tabela_nota_filosofia()
    criar_tabela_nota_geografia()
    criar_tabela_nota_matematica()
    criar_tabela_nota_portugues()
    criar_tabela_nota_fisica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM alunos")
    return cursor.fetchall()

def buscar_nota_por_materia_portugues(usuario_id):
    criar_tabela_nota_portugues()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM portugues WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_matematica(usuario_id):
    criar_tabela_nota_matematica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM matematica WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_geografia(usuario_id):
    criar_tabela_nota_geografia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM geografia WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_filosofia(usuario_id):
    criar_tabela_nota_filosofia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM filosofia WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_historia(usuario_id):
    criar_tabela_nota_historia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM historia WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_biologia(usuario_id):
    criar_tabela_nota_biologia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM biologia WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_fisica(usuario_id):
    criar_tabela_nota_fisica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM fisica WHERE usuario_id={usuario_id}")
    return cursor.fetchone()

def buscar_nota_por_materia_portugues_all(turma):
    criar_tabela_nota_portugues()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM portugues WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_nota_por_materia_matematica_all(turma):
    criar_tabela_nota_matematica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM matematica WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_nota_por_materia_geografia_all(turma):
    criar_tabela_nota_geografia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM geografia WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_nota_por_materia_filosofia_all(turma):
    criar_tabela_nota_filosofia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM filosofia WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_nota_por_materia_historia_all(turma):
    criar_tabela_nota_historia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM historia WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_nota_por_materia_biologia_all(turma):
    criar_tabela_nota_biologia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM biologia WHERE turma='{turma}'")
    return cursor.fetchall()

def buscar_nota_por_materia_fisica_all(turma):
    criar_tabela_nota_fisica()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT rowid,* FROM fisica WHERE turma='{turma}'")
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

def buscar_todos_alunos_com_nota_biologia():
    criar_tabela_nota_biologia()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN biologia n ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_todos_alunos_com_nota_fisica():
    criar_tabela_nota_fisica()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN fisica n ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_todos_alunos_com_nota_historia():
    criar_tabela_nota_historia()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN historia n ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_todos_alunos_com_nota_filosofia():
    criar_tabela_nota_filosofia()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN filosofia n ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_todos_alunos_com_nota_geografia():
    criar_tabela_nota_geografia()
    criar_tabela_nota_matematica()
    criar_tabela_nota_portugues()
    criar_tabela_nota_fisica()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN geografia n ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_todos_alunos_com_nota_matematica():
    criar_tabela_nota_historia()
    criar_tabela_nota_filosofia()
    criar_tabela_nota_geografia()
    criar_tabela_nota_matematica()
    criar_tabela_nota_portugues()
    criar_tabela_nota_fisica()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN matematica n ON a.usuario_id = n.usuario_id")
    return cursor.fetchall()

def buscar_todos_alunos_com_nota_portugues():
    criar_tabela_nota_portugues()
    criar_tabela_alunos()
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(f"SELECT a.rowid, a.nome, a.turma, n.nota1, n.nota2, n.nota3, a.falta FROM alunos a JOIN portugues n ON a.usuario_id = n.usuario_id")
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
    cursor.execute(f"UPDATE professores set excluida={True} WHERE cpf={cpf}")
    banco.commit()
    banco.close()   



if __name__ == "__main__":
    criar_tabela_usuario()
    inserir_usuario("root", "123", "Secretaria", False)    
