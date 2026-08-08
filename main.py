from repositories.funcionario_repository import FuncionarioRepository


def main():

    repository = FuncionarioRepository()

    funcionarios = repository.listar()

    if len(funcionarios) == 0:

        print("Nenhum funcionário cadastrado.")

    else:

        for funcionario in funcionarios:

            print(funcionario)

            print("-" * 50)

    repository.fechar()


if __name__ == "__main__":

    main()