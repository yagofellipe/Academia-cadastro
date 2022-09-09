from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
          host="localhost",
          user="root", 
          passwd ="", 
          database ="alunos")


def funcao_principal():
    nome_aluno = str(cadastro.nomealuno.text())
    email_aluno = str(cadastro.email.text())
    idade_aluno = str(cadastro.idade.text())
    celular_aluno = str(cadastro.celular.text())
    pagamento_aluno = str(cadastro.tipo_pagamento.currentText())
    pacote_aluno = str(cadastro.tipo_pacote.currentText())
    print("teste")
    print(nome_aluno)
    
    cursor = conexao.cursor() 
    comando = """INSERT INTO aluno (Nome, email, idade, celular, pagamento, pacote) VALUES   
    (%s,%s,%s,%s,%s,%s)"""
    dados = (nome_aluno,email_aluno,idade_aluno,celular_aluno,pagamento_aluno,pacote_aluno) 
    cursor.execute(comando,dados)
    conexao.commit()
    """Limpar os campos"""
    cadastro.nomealuno.setText()
    cadastro.email.setText()
    cadastro.idade.setText()
    cadastro.celular.setText()
    cadastro.tipo_pagamento.setText()
    cadastro.tipo_pacote.setText()
    
app = QtWidgets.QApplication([])
cadastro = uic.loadUi("janela.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()
