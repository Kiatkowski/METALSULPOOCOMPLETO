from repositories.funcionario_repository import FuncionarioRepository
from models.funcionario import Funcionario
from datetime import date
from models.funcionario import Funcionario


class Menu:
    def __init__(self):
        self.repository = FuncionarioRepository()

#futuro submenu funcionario
    def exibir(self):

        while True:
            print()
            print("-"*60)
            print("METALSUL - SISTEMA DE GERENCIAMENTO")
            print("-"*60)
            print("1. Cadastrar Funcionário")
            print("2. Buscar Funcionário")
            print("3. Listar Funcionários")
            print("4. Atualizar Funcionário")
            print("5. Excluir Funcionário")
            print("0. Sair")
            print("-"*60)

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar_funcionario()
            elif opcao == "2":
                self.buscar_funcionario()
            elif opcao == "3":
                self.listar_funcionarios()
            elif opcao == "4":
                self.atualizar_funcionario()
            elif opcao == "5":
                self.excluir_funcionario()
            elif opcao == "0":
                print("Saindo do sistema...")
                self.repository.db.fechar()
                break
            else:
                print("Opção inválida. Tente novamente.")


    def cadastrar_funcionario(self):

        print()
        print("=" * 60)
        print("CADASTRO DE FUNCIONÁRIO")
        print("=" * 60)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        sexo = input("Sexo (M/F): ").upper()
        estado_civil = input("Estado Civil: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        celular = input("Celular: ")
        cargo = input("Cargo: ")
        departamento = input("Departamento: ")
        salario = float(input("Salário: "))
        turno = input("Turno: ")

        funcionario = Funcionario(
            nome=nome,
            cpf=cpf,
            rg=rg,
            data_nascimento=None,
            sexo=sexo,
            estado_civil=estado_civil,
            email=email,
            telefone=telefone,
            celular=celular,
            cargo=cargo,
            departamento=departamento,
            salario=salario,
            data_admissao=date.today(),
            data_demissao=None,
            turno=turno,
            status="ATIVO",
            observacoes=""
        )
        self.repository.salvar(funcionario)
        print()
        input("Pressione ENTER para continuar...")

    def buscar_funcionario(self):
        pass
    def listar_funcionarios(self):
        pass
    def atualizar_funcionario(self):
        pass
    def excluir_funcionario(self):
        pass

        