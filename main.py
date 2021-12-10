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
        tela_login.erro.setText("Usuario nao encontrado.")
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
                tela_login.erro.setText("Conta nao encontrada.")
            elif aluno[6] == True:
                tela_login.erro.setText("Sua conta esta atualmente desativada, favor contatar secretaria para reativar.")
            else:
                tela_alunos.labelnomebemvindo.setText(f"{aluno[1]}")
                biologia= banco.buscar_nota_por_materia_biologia(aluno[8])
                filosofia = banco.buscar_nota_por_materia_filosofia(aluno[8])
                fisica = banco.buscar_nota_por_materia_fisica(aluno[8])
                geografia = banco.buscar_nota_por_materia_geografia(aluno[8])
                historia = banco.buscar_nota_por_materia_historia(aluno[8])
                matematica = banco.buscar_nota_por_materia_matematica(aluno[8])
                portugues = banco.buscar_nota_por_materia_portugues(aluno[8])        
                if aluno[4] == 350: # 50 dias * 7 materias.
                    tela_alunos.labelaprovadoreprovado.setText("RPF.")
                    tela_alunos.labelaluno.setText(f"{aluno[1]}")
                    tela_alunos.labelturmacar.setText(f"{aluno[2]}")
                    tela_alunos.labelcpf.setText(f"{aluno[3]}")
                    tela_alunos.data_atual.setText(str(date.today()))
                #Adicionar notas do aluno na tabela.
                else:
                    tela_alunos.labelaluno.setText(f"{aluno[1]}")
                    tela_alunos.labelturmacar.setText(f"{aluno[2]}")
                    tela_alunos.labelcpf.setText(f"{aluno[3]}")
                    tela_alunos.data_atual.setText(str(date.today()))
                    tabela = tela_alunos.tabelaboletim
                    tabela.setRowCount(7)
                    row = 0
                    count_failure = 0
                    count_sucess = 0
                    count = 0
                    search_notas = verificar_materia_notas_alunos_boletim(verificar_usuario[0])
                    if biologia != None:
                        inserir_tabela_boletim(biologia,"Biologia",aluno[4], 1)
                    if geografia != None:
                        inserir_tabela_boletim(geografia,"Geografia",aluno[4], 2)
                    if fisica != None:
                        inserir_tabela_boletim(fisica,"Fisica",aluno[4], 3)
                    if filosofia != None:
                        inserir_tabela_boletim(filosofia,"Filosofia",aluno[4], 4)
                    if matematica != None:
                        inserir_tabela_boletim(matematica,"Matematica",aluno[4], 5)
                    if portugues != None:
                        inserir_tabela_boletim(portugues,"Portugues",aluno[4], 6)
                    if historia != None:
                        inserir_tabela_boletim(historia,"Historia",aluno[4], 7)
                    if search_notas != []:
                        if biologia != None and filosofia != None and fisica != None and geografia != None and historia != None and matematica != None and portugues!= None:
                            if biologia[3] != '' and filosofia[3] != '' and fisica[3] != '' and geografia[3] != '' and historia[3] != '' and matematica[3] != '' and portugues[3] != '':
                                soma = somar_materia(biologia[1],biologia[2],biologia[3])
                                soma = somar_materia(filosofia[1],filosofia[2],filosofia[3])
                                soma = somar_materia(fisica[1],fisica[2],fisica[3])
                                soma = somar_materia(geografia[1],geografia[2],geografia[3])
                                soma = somar_materia(historia[1],historia[2],historia[3])
                                soma = somar_materia(matematica[1],matematica[2],matematica[3])
                                soma = somar_materia(portugues[1],portugues[2],portugues[3])
                                tot_soma = soma
                                if tot_soma < 7.0:
                                    count_failure += 1
                                else:
                                    count_sucess += 1
                                if count_failure > 1:
                                    tela_alunos.labelaprovadoreprovado.setText("Reprovado")
                                    tela_login.close()
                                    tela_alunos.show()
                                else:
                                    tela_alunos.labelaprovadoreprovado.setText("Aprovado")
                                    tela_login.close()
                                    tela_alunos.show()
                        else:
                            tela_login.close()
                            tela_alunos.show()
                    else:
                        tela_login.close()
                        tela_alunos.show()
        elif verificar_usuario[3] == "Professor":
            tela_professores.show()
            tela_login.close()

def somar_materia(x, x1, x2):
    soma = (int(x) + int(x1) + int(x2))
    tot_soma = soma / 3
    return tot_soma

def inserir_no_banco_todas_notas(nota1, nota2, nota3, turma, usuario_id):
    banco.inserir_notas_aluno_biologia(nota1, nota2, nota3, turma, usuario_id)
    banco.inserir_notas_aluno_geografia(nota1, nota2, nota3, turma, usuario_id)
    banco.inserir_notas_aluno_filosofia(nota1, nota2, nota3, turma, usuario_id)
    banco.inserir_notas_aluno_fisica(nota1, nota2, nota3, turma, usuario_id)
    banco.inserir_notas_aluno_historia(nota1, nota2, nota3, turma, usuario_id)
    banco.inserir_notas_aluno_matematica(nota1, nota2, nota3, turma, usuario_id)
    banco.inserir_notas_aluno_portugues(nota1, nota2, nota3, turma, usuario_id)

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
        verificar_user_alun = banco.buscar_aluno_por_cpf(cpf)
        verificar_existencia_usuario = banco.buscar_usuario(usuario)
        if verificar_user != None or verificar_user_alun != None:
            tela_registro.aviso.setText("Erro! CPF Ja registrado!")
        elif verificar_existencia_usuario != None:
            tela_registro.aviso.setText("Erro! Usuario Ja utilizado!")
        else:
            tela_registro.aviso.setText("")
            banco.inserir_usuario(usuario, senha, "Professor", False)
            verificar_existencia_usuario = banco.buscar_usuario(usuario)
            banco.inserir_professor(nome,cpf,turma, materia, False, verificar_existencia_usuario[0])        
            tela_registro.aviso.setText("Sucesso no registro.")

def inserir_tabela_boletim(materia, nome, falta, row):
    row += 1
    tabela = tela_alunos.tabelaboletim
    tabela.setRowCount(7)
    if materia != None:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{materia[1]}"))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{materia[2]}"))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{materia[3]}"))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nome}"))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{falta}"))

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
        ven_aluno = banco.buscar_aluno_por_nome_e_turma(nome, turma)
        verificar_cpf = banco.buscar_aluno_por_cpf(cpf)
        verificar_cpf_prof = banco.buscar_professor_por_cpf(cpf)
        verificar_usuario = banco.buscar_usuario(usuario)
        if verificar_cpf != None or verificar_cpf_prof != None:
            tela_registro.erro.setText("Erro! CPF Ja registrado!")
        elif verificar_usuario != None:
            tela_registro.erro.setText("Erro! Usuario Ja utilizado!")
        else:
            tela_registro.erro.setText("")
            if ven_aluno != None:
                nome = f'{nome}-{usuario}'    
                banco.inserir_usuario(usuario,senha, "Aluno", False)
                verificar_usuario = banco.buscar_usuario(usuario)
                banco.inserir_aluno(nome, turma, cpf, 0, curso, data_de_nascimento, False, verificar_usuario[0])            
                inserir_no_banco_todas_notas('','','',turma, verificar_usuario[0])
                tela_registro.erro.setText("Sucesso no registro.")
            else:
                banco.inserir_usuario(usuario, senha, "Aluno", False)
                verificar_usuario = banco.buscar_usuario(usuario)
                banco.inserir_aluno(nome, turma, cpf, 0, curso, data_de_nascimento, False, verificar_usuario[0])            
                inserir_no_banco_todas_notas('','','',turma, verificar_usuario[0])
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
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{pu[5]}"))
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

def verificar_materia_com_nota(materia):
    if materia == "Biologia":
        nota = banco.buscar_todos_alunos_com_nota_biologia()
    elif materia == "Matematica":
        nota = banco.buscar_todos_alunos_com_nota_matematica()
    elif materia == "Portugues":
        nota = banco.buscar_todos_alunos_com_nota_portugues()
    elif materia == "Fisica":
        nota = banco.buscar_todos_alunos_com_nota_fisica()
    elif materia == "Historia":
        nota = banco.buscar_todos_alunos_com_nota_historia()
    elif materia == "Geografia":
        nota = banco.buscar_todos_alunos_com_nota_geografia()
    elif materia == "Filosofia":
        nota = banco.buscar_todos_alunos_com_nota_filosofia()
    return nota

def buscar_aluno_tela_professor():
    user = tela_login.inputnome.text()
    nome = tela_professores.inputbuscaraluno.text()
    turma = tela_professores.comboturmas.currentText()
    tabela = tela_professores.tablealunosprof
    user_i = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(user_i[0])
    quant_row = 0
    if turma == 'Todas' and nome == '':
        tela_professores.label_erro.setText("ERRO! Nenhum nome informado.")
    elif turma != 'Todas' and nome == '':
        tela_professores.label_erro.setText("")
        search_notas = verificar_materia_com_nota(prof[4])
        if search_notas is None:
            tela_professores.label_erro.setText("ERRO! Nenhum aluno encontrado.")
        else:
            tabela.clearContents()
            tabela.setRowCount(len(search_notas))
            for x in search_notas:
                tabela.setItem(quant_row, 0, QtWidgets.QTableWidgetItem(f"{x[1]}"))
                tabela.setItem(quant_row, 1, QtWidgets.QTableWidgetItem(f"{x[2]}"))
                tabela.setItem(quant_row, 2, QtWidgets.QTableWidgetItem(f"{x[3]}"))
                tabela.setItem(quant_row, 3, QtWidgets.QTableWidgetItem(f"{x[4]}"))
                tabela.setItem(quant_row, 4, QtWidgets.QTableWidgetItem(f"{x[5]}"))
                tabela.setItem(quant_row, 5, QtWidgets.QTableWidgetItem(f"{x[6]}"))
                quant_row += 1
    elif turma != '' and nome != '':
        tela_professores.label_erro.setText("")
        searched = banco.buscar_aluno_por_nome_e_turma(nome, turma)
        if searched is None:
            tela_professores.label_erro.setText("Nenhum Aluno encontrado.")
        else:
            tela_professores.label_erro.setText("")
            search_notas = verificar_materia(prof[4], searched[7])
            tabela.clearContents()
            tabela.setRowCount(1)
            if search_notas is None:
                tabela.setItem(quant_row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                tabela.setItem(quant_row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                tabela.setItem(quant_row, 2, QtWidgets.QTableWidgetItem(f""))
                tabela.setItem(quant_row, 3, QtWidgets.QTableWidgetItem(f""))
                tabela.setItem(quant_row, 4, QtWidgets.QTableWidgetItem(f""))
                tabela.setItem(quant_row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
            else:
                tabela.setItem(quant_row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                tabela.setItem(quant_row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                tabela.setItem(quant_row, 2, QtWidgets.QTableWidgetItem(f"{search_notas[1]}"))
                tabela.setItem(quant_row, 3, QtWidgets.QTableWidgetItem(f"{search_notas[2]}"))
                tabela.setItem(quant_row, 4, QtWidgets.QTableWidgetItem(f"{search_notas[3]}"))
                tabela.setItem(quant_row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))

def verificar_materia(materia,user_id):
    if materia == "Biologia":
        nota_materia= banco.buscar_nota_por_materia_biologia(user_id)
    elif materia == "Filosofia":
        nota_materia = banco.buscar_nota_por_materia_filosofia(user_id)
    elif materia == "Fisica":
        nota_materia = banco.buscar_nota_por_materia_fisica(user_id)
    elif materia == "Geografia":
        nota_materia = banco.buscar_nota_por_materia_geografia(user_id)
    elif materia == "Historia":
        nota_materia = banco.buscar_nota_por_materia_historia(user_id)
    elif materia == "Matematica":
        nota_materia = banco.buscar_nota_por_materia_matematica(user_id)
    elif materia == "Portugues":
        nota_materia = banco.buscar_nota_por_materia_portugues(user_id)            
    return nota_materia    

def verificar_materia_notas_alunos_boletim(user_id):
    biologia= banco.buscar_nota_por_materia_biologia(user_id)
    filosofia = banco.buscar_nota_por_materia_filosofia(user_id)
    fisica = banco.buscar_nota_por_materia_fisica(user_id)
    geografia = banco.buscar_nota_por_materia_geografia(user_id)
    historia = banco.buscar_nota_por_materia_historia(user_id)
    matematica = banco.buscar_nota_por_materia_matematica(user_id)
    portugues = banco.buscar_nota_por_materia_portugues(user_id)            
    return biologia, filosofia, fisica,  geografia, historia, matematica, portugues  

def verificar_materia_all(materia, turma):
    if materia == "Biologia":
        nota_materia= banco.buscar_nota_por_materia_biologia_all(turma)
    elif materia == "Filosofia":
        nota_materia = banco.buscar_nota_por_materia_filosofia_all(turma)
    elif materia == "Fisica":
        nota_materia = banco.buscar_nota_por_materia_fisica_all(turma)
    elif materia == "Geografia":
        nota_materia = banco.buscar_nota_por_materia_geografia_all(turma)
    elif materia == "Historia":
        nota_materia = banco.buscar_nota_por_materia_historia_all(turma)
    elif materia == "Matematica":
        nota_materia = banco.buscar_nota_por_materia_matematica_all(turma)
    elif materia == "Portugues":
        nota_materia = banco.buscar_nota_por_materia_portugues_all(turma)            
    return nota_materia    


def add_nota_para_aluno():
    user = tela_login.inputnome.text()
    aluno = tela_professores.inputbuscaraluno.text()
    nota = tela_professores.inputaddnota.text()
    turma = tela_professores.comboturmas.currentText()
    user_i = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(user_i[0])
    ven_alun = banco.buscar_aluno_por_nome_e_turma(aluno, turma)
    tabela = tela_professores.tablealunosprof
    def_nota = tela_professores.combonotas.currentText()
    row = 0
    if aluno == "" or nota == "" or turma == "":
        tela_professores.label_erro.setText("ERRO! Campo(s) em branco.")
    elif ven_alun is None:
        tela_professores.label_erro.setText("Nenhum Aluno encontrado.")
    elif int(nota) > 10:
        tela_professores.label_erro.setText("ERRO! Nota invalida.")
    else:
        searched = banco.buscar_aluno_por_nome_e_turma(aluno, turma)
        if searched is None:
            tela_professores.label_erro.setText("Nenhum Aluno encontrado.")
        else:
            tabela.setRowCount(1)
            nota_materia = verificar_materia(prof[4], searched[7]) 
            if def_nota == "Nota 1":
                if prof[4] == "Matematica":
                    if nota_materia is None:
                        banco.editar_notas_aluno_matematica(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
                elif prof[4] == "Portugues":
                    if nota_materia is None:
                        banco.editar_notas_aluno_portugues(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
                elif prof[4] == "Geografia":
                    if nota_materia is None:
                        banco.editar_notas_aluno_geografia(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
                elif prof[4] == "Filosofia":
                    if nota_materia is None:
                        banco.editar_notas_aluno_filosofia(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
                elif prof[4] == "Historia":
                    if nota_materia is None:
                        banco.editar_notas_aluno_historia(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
                elif prof[4] == "Biologia":
                    if nota_materia is None:
                        banco.editar_notas_aluno_biologia(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
                elif prof[4] == "Fisica":
                    if nota_materia is None:
                        banco.editar_notas_aluno_fisica(str(nota),'','', searched[1], searched[7])
                        nota_materia = verificar_materia(prof[4], searched[7])
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    else:
                        tela_professores.label_erro.setText("Aluno ja possui nota no primeiro trimestre.")
                        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                        tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))        
            elif def_nota == "Nota 2":
                tela_professores.label_erro.clear()
                if prof[4] == "Biologia":
                    nota_materia= banco.buscar_nota_por_materia_biologia(searched[7])
                elif prof[4] == "Filosofia":
                    nota_materia = banco.buscar_nota_por_materia_filosofia(searched[7])
                elif prof[4] == "Fisica":
                    nota_materia = banco.buscar_nota_por_materia_fisica(searched[7])
                elif prof[4] == "Geografia":
                    nota_materia = banco.buscar_nota_por_materia_geografia(searched[7])
                elif prof[4] == "Historia":
                    nota_materia = banco.buscar_nota_por_materia_historia(searched[7])
                elif prof[4] == "Matematica":
                    nota_materia = banco.buscar_nota_por_materia_matematica(searched[7])
                elif prof[4] == "Portugues":
                    nota_materia = banco.buscar_nota_por_materia_portugues(searched[7])
                if nota_materia is None:
                    tela_professores.label_erro.setText("ERRO! Aluno nao possui nota no primeiro trimestre.")                
                elif nota_materia[2] != "":
                    tela_professores.label_erro.setText("ERRO! aluno ja possui nota no segundo trimestre.")                
                else:
                    if prof[4] == "Matematica":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_matematica(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Portugues":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_portugues(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Geografia":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_geografia(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Filosofia":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_filosofia(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Historia":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_historia(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Biologia":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_biologia(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Fisica":
                        if nota_materia[2] == '':
                            banco.editar_notas_aluno_matematica(nota_materia[1],str(nota),'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
            elif def_nota == "Nota 3":
                tela_professores.label_erro.clear()
                nota_materia = verificar_materia(prof[4], searched[7])
                if nota_materia is None:
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno nao possui nota no primeiro trimestre.")
                elif nota_materia[1] == '':
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno nao possui nota no primeiro trimestre.")
                elif nota_materia[2] == '':
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno nao possui nota no segundo trimestre.")
                elif nota_materia[3] != "":
                    tela_professores.label_erro.setText("Nota nao adicionada, aluno ja possui nota no terceiro trimestre.")                
                    tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                    tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                    tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                    tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                    tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                    tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                else:
                    if prof[4] == "Matematica":
                            banco.editar_notas_aluno_matematica(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Portugues":
                            banco.editar_notas_aluno_portugues(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Geografia":
                            banco.editar_notas_aluno_geografia(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Filosofia":
                            banco.editar_notas_aluno_filosofia(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Historia":
                            banco.editar_notas_aluno_historia(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Biologia":
                            banco.editar_notas_aluno_biologia(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
                    elif prof[4] == "Fisica":
                            banco.editar_notas_aluno_fisica(nota_materia[1],nota_materia[2],'', searched[1], searched[7])
                            nota_materia = verificar_materia(prof[4], searched[7])
                            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
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
    elif int(nota) > 10:
        tela_professores.label_erro.setText("Nota invalida.")
    else:
        searched = banco.buscar_aluno_por_nome_e_turma(aluno, turma)
        if searched is None:
            tela_professores.label_erro.setText("Nenhum Aluno encontrado.")
        else:
            nota_materia = verificar_materia(prof[4], searched[7])
            tabela.setRowCount(1)
            if nota_materia is None:
                tela_professores.label_erro.setText("Nenhuma nota encontrada.")
            elif def_nota == "Nota 1":
                tela_professores.label_erro.setText("")
                b = verificar_materia(prof[4], searched[7])
                if b[1] == '':
                    tela_professores.label_erro.setText("Aluno nao possui nota para mudanca.")
                else:
                    if prof[4] == "Matematica":
                        banco.editar_notas_aluno_matematica(nota, b[2], b[3], searched[1], searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    elif prof[4] == "Portugues":
                        banco.editar_notas_aluno_portugues(nota, b[2], b[3], searched[1], searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    elif prof[4] == "Fisica":
                        banco.editar_notas_aluno_fisica(nota, b[2], b[3], searched[1], searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    elif prof[4] == "Geografia":
                        banco.editar_notas_aluno_geografia(nota, b[2], b[3], searched[1], searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    elif prof[4] == "Historia":
                        banco.editar_notas_aluno_historia(nota, b[2], b[3], searched[1], searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    elif prof[4] == "Filosofia":
                        banco.editar_notas_aluno_filosofia(nota, b[2], b[3], searched[1],searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    elif prof[4] == "Biologia":
                        banco.editar_notas_aluno_biologia(nota, b[2], b[3], searched[1], searched[7])
                        b = verificar_materia(prof[4], searched[7])
                        tela_professores.label_erro.setText("Nota Alterada.")
                    nota_materia = verificar_materia(prof[4], searched[7])
                    tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                    tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                    tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                    tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                    tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                    tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
            elif def_nota == "Nota 2":
                tela_professores.label_erro.setText("")
                if prof[4] == "Matematica":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Portugues":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Fisica":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Geografia":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Historia":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Filosofia":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Biologia":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_matematica(b[1], nota, b[3], searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                nota_materia = verificar_materia(prof[4], searched[7])
                tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))
            elif def_nota == "Nota 3":
                if prof[4] == "Matematica":
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                    tela_professores.label_erro.setText("Nota Alterada.")
                if prof[4] == "Portugues":
                    tela_professores.label_erro.setText("Nota Alterada.")
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                if prof[4] == "Fisica":
                    tela_professores.label_erro.setText("Nota Alterada.")
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                if prof[4] == "Geografia":
                    tela_professores.label_erro.setText("Nota Alterada.")
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                if prof[4] == "Historia":
                    tela_professores.label_erro.setText("Nota Alterada.")
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                if prof[4] == "Filosofia":
                    tela_professores.label_erro.setText("Nota Alterada.")
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                if prof[4] == "Biologia":
                    tela_professores.label_erro.setText("Nota Alterada.")
                    b = verificar_materia(prof[4], searched[7])
                    banco.editar_notas_aluno_biologia(b[1], b[2], nota, searched[1], searched[7])
                nota_materia = verificar_materia(prof[4], searched[7])
                tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{searched[0]}"))
                tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{searched[1]}"))
                tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{nota_materia[1]}"))
                tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{nota_materia[2]}"))
                tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f"{nota_materia[3]}"))
                tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{searched[3]}"))

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
                tela_registro.avisor.setText("Conta do aluno desativada com sucesso.")
        elif btnprofessor == True:
            if ven_cpf_prof is None:
                tela_registro.avisor.setText("Nenhum professor encontrado.")
            else:
                tela_registro.avisor.setText("")
                banco.deletar_professor_por_cpf(cpf)
                tela_registro.avisor.setText("Conta do professor desativada com sucesso.")
        else:
            tela_registro.avisor.setText("Por favor escolha uma opcao.")

def mostrar_minhas_turmas_professor():
    tela_minhas_turmas_professor.show()
    user = tela_login.inputnome.text()
    ven_user = banco.buscar_usuario(user)
    prof = banco.buscar_professor_user_id(ven_user[0])
    turma = prof[3]
    turma = str(turma)[1:-1]
    tela_minhas_turmas_professor.label_3.setText(f"{turma}")
    tela_professores.close()

def voltar_tela_minhas_turmas_prof():
    tela_minhas_turmas_professor.close()
    tela_professores.show()

def adicionar_falta_para_aluno():
    aluno = tela_professores.inputbuscaraluno.text()
    turma = tela_professores.comboturmas.currentText()
    row = 0
    if aluno == '' or turma == '':
        tela_professores.label_erro.setText("Campo(s) invalido(s).")
    else:
        tela_professores.label_erro.setText("")
        ven_alun = banco.buscar_aluno_por_nome_e_turma(aluno,turma)
        tabela = tela_professores.tablealunosprof
        if ven_alun is None:
            tela_professores.label_erro.setText("Nenhum aluno encontrado.")
        else:
            tabela.setItem(row, 5, QtWidgets.QTableWidgetItem(f"{ven_alun[3]}"))
            falta = int(ven_alun[3]) + 1
            banco.editar_falta_aluno(falta, ven_alun[7])
            tela_professores.label_erro.setText("Falta Inserida.")

def fechar_tela_aviso():
    tela_aviso.close()

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
    tela_aviso = uic.loadUi('aviso.ui')
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

    tela_aviso.btnok.clicked.connect(fechar_tela_aviso)

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