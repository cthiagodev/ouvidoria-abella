# 📢 Sistema de Ouvidoria em Python

Este é um sistema de ouvidoria simples feito em Python que permite registrar, listar, pesquisar e excluir manifestações (reclamações, sugestões, elogios etc.) armazenadas em um banco de dados MySQL.

## 🧰 Funcionalidades

O sistema oferece as seguintes opções por meio de um menu interativo:

1. **Listar todas as manifestações**  
2. **Adicionar nova manifestação**  
3. **Exibir quantidade de manifestações**  
4. **Pesquisar manifestação por código**  
5. **Excluir manifestação por código**  
6. **Listar manifestações por tipo**  
7. **Sair do sistema**

## 🛠️ Pré-requisitos

- Python 3.x  
- MySQL Server  
- Biblioteca `mysql-connector-python`  
- Arquivo `operacoesbd.py` com as seguintes funções:
  - `criarConexao(host, usuario, senha, nome_banco)`
  - `listarBancoDados(conexao, sql, dados=[])`
  - `insertNoBancoDados(conexao, sql, dados)`
  - `excluirBancoDados(conexao, sql, dados)`
  - `encerrarConexao()`

## 🗃️ Estrutura esperada do banco de dados

Banco de dados: `ouvidoria`  
Tabela: `manifestacoes`

```sql
CREATE TABLE manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    descricao TEXT
);
```

## ⚙️ Como executar

1. Clone este repositório ou copie os arquivos para seu ambiente local.
2. Certifique-se de que o MySQL está em execução e o banco de dados `ouvidoria` foi criado com a tabela `manifestacoes`.
3. Atualize as credenciais de conexão no script principal, se necessário:
   ```python
   conexao = criarConexao("localhost", "root", "123456", "ouvidoria")
   ```
4. Execute o script:
   ```bash
   python main.py
   ```

## 📝 Exemplo de uso

```
Bem vindo à nossa ouvidoria:

MENU DE OPÇÕES:
1) Listar todas as manifestações
2) Adicionar nova manifestação
3) Exibir quantidade de manifestações
4) Pesquisar manifestação por código
5) Excluir manifestação por código
6) Listar manifestações por tipo
7) Sair
```
