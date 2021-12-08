from sqlite3.dbapi2 import Row
import sys, banco
from PyQt5 import uic, QtWidgets
from datetime import date



#########################################################################################################################
#                                              Sistema Academico                                                        #
#         Secretaria - Gerencia registramento de professores e dos horarios escolares                                   #
#         Professor - Adiciona Notas e gerencia falta(s) do aluno.                                                      #
#         Aluno - Checa suas notas de certas materias, assim como seu resultado final (Aprovado, Reprovado).            #
#                                                                                                                       #
#                                                                                                                       #
#########################################################################################################################

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
        if verificar_usuario[3] == "Secretaria":
            for i in range(1990,2021):
                tela_registro.ano.addItem(f"{i}")
            tela_registro.show()
            tela_login.close()
        elif verificar_usuario[3] == "Aluno":
            aluno = banco.buscar_aluno_por_id(verificar_usuario[0])
            if aluno is None:
                tela_login.erro.setText("Sua conta foi deletada, favor contatar secretaria.")
            else:
                notas = banco.buscar_notas(aluno[6])
                faltas = banco.buscar_faltas_por_user_id(aluno[6])
                tela_alunos.labelnomebemvindo.setText(f"{aluno[1]}")
                if faltas == []:
                    tela_alunos.labelaprovadoreprovado.setText("")
                elif faltas == ["350"]: # 50 dias * 7 materias.
                    tela_alunos.labelaprovadoreprovado.setText("Reprovado por falta.")
                tela_alunos.labelaluno.setText(f"{aluno[1]}")
                tela_alunos.labelturmacar.setText(f"{aluno[2]}")
                tela_alunos.labelcpf.setText(f"{aluno[3]}")
                tela_alunos.data_atual.setText(str(date.today()))
                #Adicionar notas do aluno na tabela.
                if notas == []:
                    tela_alunos.show()
                    tela_login.close()
                else:
                    tabela = tela_alunos.tabelaboletim
                    tabela.setRowCount(7)
                    row = 0
                    soma = 0
                    for p in notas:
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{p[1]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{p[2]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{p[3]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{p[4]}"))
                        row += 1
                    for p in notas:
                        soma = float(p[1]) + float(p[2]) + float(p[3])
                        tot_soma = soma
                        row += 1
                        if row == 2:
                            tot_soma = tot_soma / 3
                            if tot_soma < 7.0:
                                tela_alunos.labelaprovadoreprovado.setText("Reprovado")
                        if row == 5:
                            break
                    tela_alunos.show()
                    tela_login.close()
        elif verificar_usuario[3] == "Professor":
            tela_professores.show()
            tela_login.close()

def registrar_professor():
    nome = tela_registro.inputnomeprofessor.text()
    cpf = tela_registro.inputcpfprofessor.text()
    materia = tela_registro.inputmateria.currentText()
    senha = tela_registro.inputsenhaprofessor.text()
    csenha = tela_registro.inputcsenhaprofessor.text()
    usuario = tela_registro.inputusuarioprofessor.text()
    turma = []
    #Turmas do professor, professor pode dar aula para mais de uma turma.
    if tela_registro.t101.isChecked() == True:
        turma.append("101")
    if tela_registro.t102.isChecked() == True:
        turma.append("102")
    if tela_registro.t103.isChecked() == True:
        turma.append("103")
    if nome == "" or cpf == '' or senha == '' or csenha == '' or usuario == '' or turma == [] or materia == "":
        tela_registro.aviso.setText("Campo(s) em branco.")
    elif int(len(nome)) < 3:
        tela_registro.aviso.setText("Nome invalido.")
    elif len(senha) < 6:
        tela_registro.aviso.setText("Senha necessita possuir mais do que 6 caracteres.")
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
            banco.inserir_usuario(usuario, senha, "Professor")
            verificar_existencia_usuario = banco.buscar_usuario(usuario)
            banco.inserir_professor(nome,cpf,turma, materia, verificar_existencia_usuario[0])        
            tela_registro.aviso.setText("Sucesso no registro.")

def registrar_aluno():
    nome = tela_registro.inputnomealuno.text()
    cpf = tela_registro.inputcpfaluno.text()
    senha = tela_registro.inputsenhaaluno.text()
    csenha = tela_registro.inputcsenhaaluno.text()
    usuario = tela_registro.inputusuarioaluno.text()
    turma = tela_registro.turmabox.currentText()
    curso = tela_registro.cursobox.currentText()
    dia = tela_registro.dia.currentText()
    mes = tela_registro.mes.currentText()
    ano = tela_registro.ano.currentText()
    data_de_nascimento = str(f"{dia}/{mes}/{ano}") 
    if nome == "" or cpf == '' or senha == '' or csenha == '' or usuario == '' or turma == '' or curso == '' or ano == "":
        tela_registro.erro.setText("Campo(s) em branco.")
    elif csenha != senha:
        tela_registro.erro.setText("Senhas Nao coincidem!")
    elif len(senha) < 6:
        tela_registro.erro.setText("Senha necessita ter mais que 6 caracteres.")
    elif len(usuario) < 7:
        tela_registro.erro.setText("Usuario necessita ter mais que 7 caracteres.")
    elif ano == "2021" or ano == "2020":
        tela_registro.erro.setText("Data invalida.")
    elif int(len(nome)) < 3:
        tela_registro.erro.setText("Nome Invalido.")
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
            banco.inserir_aluno(nome, turma, cpf, curso, data_de_nascimento, verificar_usuario[0])            
            tela_registro.erro.setText("Sucesso no registro.")

def mostrar_alunos_minha_turma():
    tela_minha_turma.show()
    usuario = tela_login.inputnome.text()
    user = banco.buscar_usuario(usuario)
    aluno = banco.buscar_aluno_por_id(user[0])
    turma = aluno[2]
    minha_turma = banco.buscar_alunos_mesma_turma(turma)
    tela_minha_turma.labelminhaturma.setText(f"{turma}")
    tabela = tela_minha_turma.tableturmas
    tabela.setRowCount(len(minha_turma))
    row = 0
    for pu in minha_turma:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{pu[0]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{pu[4]}"))
        row += 1  

def visualizar_dados_escolares():
    usuario = tela_login.inputnome.text()
    verificar_usuario = banco.buscar_usuario(usuario)
    aluno = banco.buscar_aluno_por_id(verificar_usuario[0])
    if aluno[2] == "101":
        tela_dados_escolares_matutino.show()
    elif aluno[2] == "102":
        tela_dados_escolares_vespertino.show()
    elif aluno[2] == "103":
        tela_dados_escolares_noturno.show()

def fechar_tela_dados_escolares_matutino():
    tela_dados_escolares_matutino.close()

def fechar_tela_dados_escolares_vespertino():
    tela_dados_escolares_vespertino.close()

def fechar_tela_dados_escolares_noturno():
    tela_dados_escolares_noturno.close()

def logout():
    tela_alunos.close()
    tela_login.show()

def mostrar_tela_informacoes():
    tela_informacoes.show()

def voltar_tela_informacoes():
    tela_informacoes.close()

def voltar_tela_diretor():
    tela_registro.close()
    tela_login.show()

def buscar_aluno_tela_professor():
    user = tela_login.inputnome.text()
    nome = tela_professores.inputbuscaraluno.text()
    turma = tela_professores.comboturmas.currentText()
    tabela = tela_professores.tablealunosprof
    user_i = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(user_i[0])
    quant_row = 0
    if turma == '':
        tela_professores.label_erro.setText("Campo turma obrigatorio.")
    else:
        tela_professores.label_erro.setText("")
        info_aluno = banco.buscar_aluno_por_nome_e_turma(nome, turma)
        if nome == '':
            tela_professores.label_erro.setText("Nenhum aluno provido.")
        elif info_aluno == []:
            tela_professores.label_erro.setText("Nenhum aluno encontrado.")
        elif turma == '':
            tela_professores.label_erro.setText("Campo turma em branco.")
        else:
            tela_professores.label_erro.setText("")
            search_notas = banco.buscar_nota_por_materia(prof[4], info_aluno[0][5])
            tabela.setRowCount(len(info_aluno))
            if search_notas == []:
                for x in info_aluno:
                    tabela.setItem(quant_row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                    tabela.setItem(quant_row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                    tabela.setItem(quant_row, 2, QtWidgets.QTableWidgetItem(f"0"))
                    tabela.setItem(quant_row, 3, QtWidgets.QTableWidgetItem(f"0"))
                    tabela.setItem(quant_row, 4, QtWidgets.QTableWidgetItem(f"0"))
                    tabela.setItem(quant_row, 5, QtWidgets.QTableWidgetItem(f"{prof[4]}"))
                    quant_row += 1
            else:
                for x in info_aluno:
                    tabela.setItem(quant_row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                    tabela.setItem(quant_row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                    tabela.setItem(quant_row, 2, QtWidgets.QTableWidgetItem(f"{search_notas[0][1]}"))
                    tabela.setItem(quant_row, 3, QtWidgets.QTableWidgetItem(f"{search_notas[0][2]}"))
                    tabela.setItem(quant_row, 4, QtWidgets.QTableWidgetItem(f"{search_notas[0][3]}"))
                    tabela.setItem(quant_row, 5, QtWidgets.QTableWidgetItem(f"{prof[4]}"))
                    quant_row += 1

def add_nota_para_aluno():
    user = tela_login.inputnome.text()
    aluno = tela_professores.inputbuscaraluno.text()
    nota = tela_professores.inputaddnota.text()
    turma = tela_professores.comboturmas.currentText()
    user_i = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(user_i[0])
    tabela = tela_professores.tablealunosprof
    def_nota = tela_professores.combonotas.currentText()
    row = 0
    if aluno == "" or nota == "" or turma == "":
        tela_professores.label_erro.setText("ERRO! Campo(s) em branco.")
    elif float(nota) > 10:
        tela_professores.label_erro.setText("ERRO! Nota invalida.")
    else:
        searched = banco.buscar_aluno_por_nome_e_turma(aluno, turma)
        if searched == []:
            tela_professores.label_erro.setText("Nenhum Aluno encontrado.")
        else:
            tabela.setRowCount(1)
            if def_nota == "Nota 1":
                nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                if nota_materia != []:
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno ja possui nota no primeiro trimestre.")
                    for x in searched:
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[0][1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[0][2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[0][3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{nota_materia[0][4]}"))
                else:
                    banco.inserir_notas_aluno(str(nota),'0','0',prof[4], searched[0][5])
                    nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                    for x in searched:
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[0][1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[0][2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[0][3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{nota_materia[0][4]}"))
                        
            elif def_nota == "Nota 2":
                tela_professores.label_erro.clear()
                nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                if nota_materia == []:
                    banco.inserir_notas_aluno('0','0','0', prof[4], searched[0][5])              
                elif nota_materia[0][2] != "0":
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno ja possui nota no segundo trimestre.")                
                else:
                    banco.editar_notas_aluno(nota_materia[0][1], str(nota),'0', prof[4], searched[0][5])
                    nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                    for x in searched:
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[0][1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[0][2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[0][3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{nota_materia[0][4]}"))
            elif def_nota == "Nota 3":
                tela_professores.label_erro.clear()
                nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                if nota_materia[0][3] != "0":
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno ja possui nota no terceiro trimestre.")
                banco.editar_notas_aluno(nota_materia[0][1], nota_materia[0][2], str(nota), prof[4], searched[0][5])
                nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                for x in searched:
                    tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                    tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                    tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[0][1]}"))
                    tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[0][2]}"))
                    tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[0][3]}"))
                    tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{nota_materia[0][4]}"))
                    

def editar_nota():
    user = tela_login.inputnome.text()
    aluno = tela_professores.inputbuscaraluno.text()
    nota = tela_professores.inputaddnota.text()
    turma = tela_professores.comboturmas.currentText()
    user_i = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(user_i[0])
    tabela = tela_professores.tablealunosprof
    def_nota = tela_professores.combonotas.currentText()
    row = 0
    if aluno == "" or nota == "" or turma == "":
        tela_professores.label_erro.setText("ERRO! Campo(s) em branco.")
    else:
        searched = banco.buscar_aluno_por_nome_e_turma(aluno, turma)
        nota_materia = banco.buscar_nota_por_materia(prof[4], searched[0][5])
        if searched != None:
            if def_nota == "Nota 1":
                b = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                banco.editar_notas_aluno(nota, b[1], b[2], prof[4], searched[0][5])
            elif def_nota == "Nota 2":
                b = banco.buscar_nota_por_materia(prof[4], searched[0][5])
                banco.editar_notas_aluno(b[0],nota, b[2], prof[4], searched[0][5])
            elif def_nota == "Nota 3":
                b = banco.buscar_nota_por_materia(prof[4], searched[5])
                banco.editar_notas_aluno(b[0],b[1], nota, prof[4], searched[0][5])
            b = banco.buscar_nota_por_materia(prof[4], searched[0][5])
            tabela.setRowCount(len(searched))
            for x in searched:
                tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{x[0]}"))
                tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[0][1]}"))
                tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[0][2]}"))
                tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[0][3]}"))
                tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{nota_materia[0][4]}"))
                row += 1  

def remover():
    cpf = tela_registro.inputcpfdeletar.text()
    btnaluno = tela_registro.buttonaluno.isChecked()
    btnprofessor = tela_registro.buttonprofessor.isChecked()
    if cpf == '':
        tela_registro.avisor.setText("ERRO! Nenhum cpf provido.")
    else:
        tela_registro.avisor.setText("")
        ven_cpf_alun = banco.buscar_aluno_por_cpf(cpf)
        ven_cpf_prof = banco.buscar_professor_por_cpf(cpf)
        if btnaluno == True:
            if ven_cpf_alun is None:
                tela_registro.avisor.setText("Nenhum Aluno encontrado.")
            else:
                tela_registro.avisor.setText("")
                banco.deletar_aluno_por_cpf(cpf)
        elif btnprofessor == True:
            if ven_cpf_prof is None:
                tela_registro.avisor.setText("Nenhum professor encontrado.")
            else:
                tela_registro.avisor.setText("")
                banco.deletar_professor_por_cpf(cpf)
        else:
            tela_registro.avisor.setText("Por favor escolha uma opcao.")

def mostrar_minhas_turmas_professor():
    tela_minhas_turmas_professor.show()
    user = tela_login.inputnome.text()
    ven_user = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(ven_user[0])
    turma = prof[3]
    tela_minhas_turmas_professor.label_3.setText(f"{turma}")
    tela_professores.close()

def voltar_tela_minhas_turmas_prof():
    tela_minhas_turmas_professor.close()
    tela_professores.show()

def adicionar_falta_para_aluno():
    aluno = tela_professores.inputbuscaraluno.text()
    turma = tela_professores.comboturmas.currentText()
    if aluno == '' or turma == '':
        tela_professores.label_erro.setText("Campo(s) invalido(s).")
    else:
        tela_professores.label_erro.setText("")
        ven_alun = banco.buscar_aluno_por_nome_e_turma(aluno,turma)
        if ven_alun == []:
            tela_professores.label_erro.setText("Nenhum aluno encontrado.")
        else:
            pesq_aluno = banco.buscar_aluno_por_nome_e_turma(aluno,turma)
            falt = banco.buscar_faltas_por_user_id(pesq_aluno[0][5])
            if falt != []:
                falta = int(falt[0][1]) + 1
                banco.editar_falta_aluno(falta, pesq_aluno[0][5] )
                tela_professores.label_erro.setText("Falta Inserida.")
            else:
                banco.inserir_falta_para_aluno(1,pesq_aluno[0][5])
                tela_professores.label_erro.setText("Falta Inserida.")

def voltar_tela_prof():
    tela_professores.close()
    tela_login.show()

if __name__ == "__main__":
    qt = QtWidgets.QApplication(sys.argv)
    #Telas
    tela_login = uic.loadUi('login.ui')
    tela_registro = uic.loadUi('cadastro-aluno-professores.ui')
    tela_alunos = uic.loadUi('menu-aluno.ui')
    tela_minha_turma = uic.loadUi('minha-turma.ui')
    tela_professores = uic.loadUi('menu-professor.ui')
    tela_dados_escolares_matutino = uic.loadUi('101 Matutino.ui')
    tela_dados_escolares_vespertino = uic.loadUi('102 Vespertino.ui')
    tela_dados_escolares_noturno = uic.loadUi('103 Noturno.ui')
    tela_informacoes = uic.loadUi('informacoes.ui')
    tela_minhas_turmas_professor = uic.loadUi('minha-turmaprof.ui')


    #Botoes
    tela_login.btn_login.clicked.connect(logar)
    
    tela_registro.cadastrarprofessor.clicked.connect(registrar_professor)
    tela_registro.cadastraraluno.clicked.connect(registrar_aluno)
    tela_registro.btnvoltarcadastro2.clicked.connect(voltar_tela_diretor)
    tela_registro.btnvoltarcadastro_3.clicked.connect(voltar_tela_diretor)
    tela_registro.btnvoltarcadastro.clicked.connect(voltar_tela_diretor)
    tela_registro.btnremover.clicked.connect(remover)

    tela_professores.btnbuscaraluno.clicked.connect(buscar_aluno_tela_professor)
    tela_professores.editarnota.clicked.connect(editar_nota)
    tela_professores.btnadicionaraluno.clicked.connect(add_nota_para_aluno)
    tela_professores.btninformacoes.clicked.connect(mostrar_tela_informacoes)
    tela_professores.btnminhaturmaprof.clicked.connect(mostrar_minhas_turmas_professor)
    tela_professores.btnfalta.clicked.connect(adicionar_falta_para_aluno)
    tela_professores.btnlogout.clicked.connect(voltar_tela_prof)
    
    tela_alunos.btndadosescolares.clicked.connect(visualizar_dados_escolares)
    tela_alunos.btnminhaturma.clicked.connect(mostrar_alunos_minha_turma)
    tela_alunos.btnlogout.clicked.connect(logout)
    tela_alunos.btninformacoes.clicked.connect(mostrar_tela_informacoes)
    
    tela_informacoes.btnvoltar.clicked.connect(voltar_tela_informacoes)

    tela_minhas_turmas_professor.btnvoltarprof.clicked.connect(voltar_tela_minhas_turmas_prof)

    tela_dados_escolares_matutino.btnvoltar1.clicked.connect(fechar_tela_dados_escolares_matutino)
    tela_dados_escolares_vespertino.btnvoltar2.clicked.connect(fechar_tela_dados_escolares_vespertino)
    tela_dados_escolares_noturno.btnvoltar3.clicked.connect(fechar_tela_dados_escolares_noturno)
    
        
    tela_login.show()
    qt.exec_()