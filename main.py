from database.conexao import Conexao

def main():
    conexao = Conexao()
    print("Conexão com o banco de dados estabelecida com sucesso!")

    conexao.fechar()  # Fechar a conexão com o banco de dados

if __name__ == "__main__":
    main()    