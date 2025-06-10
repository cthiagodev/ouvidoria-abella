from operacoesbd import *

conexao = criarConexao("localhost", "root", "123456", "ouvidoria")

if conexao:
    opcao = 1
    print("Bem vindo à nossa ouvidoria:")

    while opcao != 7:
        print("\nMENU DE OPÇÕES:")
        print("1) Listar todas as manifestações")
        print("2) Adicionar nova manifestação")
        print("3) Exibir quantidade de manifestações")
        print("4) Pesquisar manifestação por código")
        print("5) Excluir manifestação por código")
        print("6) Listar manifestações por tipo")
        print("7) Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        print("-" * 40)
    
        if opcao == 1:
            sql = "SELECT * FROM manifestacoes"
            print(listarBancoDados(conexao, sql))
        elif opcao == 2:
            tipo = input("Digite o tipo da manifestação: ")
            descricao = input("Digite sua manifestação: ")
            sql = "INSERT INTO manifestacoes(tipo, descricao) VALUES(%s, %s)"
            dados = [tipo, descricao]
            insertNoBancoDados(conexao, sql, dados)
        elif opcao == 3:
            sql = "SELECT COUNT(*) FROM manifestacoes"
            print(listarBancoDados(conexao, sql))
        elif opcao == 4:
            sql = "SELECT * FROM manifestacoes WHERE id = %s"
            codigo_manifestacao = int(input("Digite o código da manifestação que você quer exibir: "))
            dados = [codigo_manifestacao]
            print(listarBancoDados(conexao, sql, dados))
        elif opcao == 5:
            sql = "DELETE FROM manifestacoes WHERE id = %s"
            codigo_manifestacao = int(input("Digite o código da manifestação que você quer excluir: "))
            dados = [codigo_manifestacao]
            excluirBancoDados(conexao, sql, dados)
        elif opcao == 6:
            sql = "SELECT * FROM manifestacoes WHERE tipo = %s"
            tipo_manifestacao = input("Digite o tipo da manifestação que você quer exibir: ")
            dados = [tipo_manifestacao]
            print(listarBancoDados(conexao, sql, dados))

        elif opcao == 7:
            encerrarConexao()

else:
    print("Falha na conexão com o banco de dados")