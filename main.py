import sys, banco
from PyQt5 import uic, QtWidgets

def logar():
    usuario = tela_login.inputnome.text()
    senha = tela_login.inputsenha.text()
    tela_login.erro.setText("")
    verificar_usuario = banco.buscar_usuario(usuario)
    if verificar_usuario == None:
        tela_login.erro.setText("Nome nao encontrado.")
    elif verificar_usuario[2] != senha:
        tela_login.erro.setText("Dados nao conferem.")
    else:
        if verificar_usuario[3] == "Diretor":
            tela_registro.show()
            tela_login.close()
        elif verificar_usuario[3] == "Aluno":
            aluno = banco.buscar_aluno_por_id(verificar_usuario[0])
            notas = banco.buscar_notas(aluno[9])
            if notas != None:
                tabela = tela_alunos.tabelaboletim
                tabela.setRowCount(7)
                row = 0
                for p in notas:
                    tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{p[3]}"))
                    tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{p[0]}"))
                    tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{p[1]}"))
                    tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{p[2]}"))
                    row += 1  
                    tela_alunos.show()
                    tela_login.close()
            else:
                    tela_alunos.show()
                    tela_login.close()
        elif verificar_usuario[3] == "Professor":
            #tela_professores.show()
            tela_login.close()

def registrar_professor():
    nome = tela_registro.inputnomeprofessor.text()
    sobrenome = tela_registro.inputsobrenomeprofessor.text()
    cpf = tela_registro.inputcpfprofessor.text()
    endereco = tela_registro.inputenderecoprofessor.text()
    complemento = tela_registro.inputcomplementoprofessor.text()
    materia = tela_registro.materiaprofessor.currentText()
    senha = tela_registro.inputsenhaprofessor.text()
    csenha = tela_registro.inputcsenhaprofessor.text()
    usuario = tela_registro.inputusuarioprofessor.text()
    turma = []
    if tela_registro.t101.isChecked() == True:
        turma.append("101")
    if tela_registro.t102.isChecked() == True:
        turma.append("102")
    if tela_registro.t103.isChecked() == True:
        turma.append("103")
    if nome == "" or sobrenome == '' or cpf == '' or endereco == '' or complemento == '' or senha == '' or csenha == '' or usuario == '' or turma == [] or materia == "":
        tela_registro.aviso.setText("Campo(s) em branco.")
    elif csenha != senha:
        tela_registro.aviso.setText("Senhas nao correspondem.")
    else:
        verificar_user = banco.buscar_professor_por_cpf(cpf)
        verificar_existencia_usuario = banco.buscar_usuario(usuario)
        if verificar_user != None:
            tela_registro.aviso.setText("Erro! CPF Ja registrado!")
        elif verificar_existencia_usuario != None:
            tela_registro.aviso.setText("Erro! Usuario Ja utilizado!")
        else:
            tela_registro.aviso.setText("")
            banco.inserir_professor(nome,sobrenome,cpf,endereco,complemento,turma)        
            banco.inserir_usuario(usuario, senha, "Professor")
            tela_registro.aviso.setText("Sucesso no registro.")

def registrar_aluno():
    nome = tela_registro.inputnomealuno.text()
    sobrenome = tela_registro.inputsobrenomealuno.text()
    cpf = tela_registro.inputcpfaluno.text()
    endereco = tela_registro.inputenderecoaluno.text()
    complemento = tela_registro.inputcomplementoaluno.text()
    senha = tela_registro.inputsenhaaluno.text()
    csenha = tela_registro.inputcsenhaaluno.text()
    usuario = tela_registro.inputusuarioaluno.text()
    turma = tela_registro.turmabox.currentText()
    curso = tela_registro.cursobox.currentText()
    data_de_nascimento = tela_registro.inputdatadenascimentoaluno.text()
    if nome == "" or sobrenome == '' or cpf == '' or endereco == '' or complemento == '' or senha == '' or csenha == '' or usuario == '' or turma == '' or curso == '' or data_de_nascimento == "//":
        tela_registro.erro.setText("Campo(s) em branco.")
    if nome == "Nome" or sobrenome == 'Sobrenome' or cpf == '' or endereco == 'Endereço' or complemento == 'Complemento' or senha == 'Senha' or csenha == 'Confirmar Senha' or usuario == 'Usuario' or turma == '' or curso == '' or data_de_nascimento == "//":
        tela_registro.erro.setText("Campo(s) invalido(s)!")
    elif csenha != senha:
        tela_registro.erro.setText("Senhas Nao coincidem!")
    else:
        verificar_cpf = banco.buscar_aluno_por_cpf(cpf)
        verificar_usuario = banco.buscar_usuario(usuario)
        if verificar_cpf != None:
            tela_registro.erro.setText("Erro! CPF Ja registrado!")
        elif verificar_usuario != None:
            tela_registro.erro.setText("Erro! Usuario Ja utilizado!")
        else:
            tela_registro.erro.setText("")
            banco.inserir_usuario(usuario,senha, "Aluno")
            verificar_usuario = banco.buscar_usuario(usuario)
            banco.inserir_aluno(nome, sobrenome, cpf, endereco, complemento, curso, data_de_nascimento, turma, verificar_usuario[0])            
            tela_registro.erro.setText("Sucesso no registro.")

def mostrar_alunos_minha_turma():
    tela_minha_turma.show()
    usuario = tela_login.inputnome.text()
    user = banco.buscar_usuario(usuario)
    aluno = banco.buscar_aluno_por_id(user[0])
    turma = aluno[6]
    minha_turma = banco.buscar_alunos_mesma_turma(turma)
    tela_minha_turma.labelminhaturma.setText(f"{turma}")
    tabela = tela_minha_turma.tableturmas
    tabela.setRowCount(len(minha_turma))
    row = 0
    for pu in minha_turma:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{pu[1]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{pu[8]}"))
        row += 1  

















if __name__ == "__main__":
    qt = QtWidgets.QApplication(sys.argv)
    #Telas
    tela_login = uic.loadUi('login.ui')
    tela_registro = uic.loadUi('cadastro-aluno-professores.ui')
    tela_alunos = uic.loadUi('menu-aluno.ui')
    tela_minha_turma = uic.loadUi('minha-turma.ui')
    
    #Botoes
    tela_login.btn_login.clicked.connect(logar)
    tela_registro.cadastrarprofessor.clicked.connect(registrar_professor)
    tela_registro.cadastraraluno.clicked.connect(registrar_aluno)
    tela_alunos.btnminhaturma.clicked.connect(mostrar_alunos_minha_turma)
    tela_login.show()
    qt.exec_()