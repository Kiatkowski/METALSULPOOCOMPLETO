from datetime import date

from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository


class Menu:
    def __init__(self):
        self.repository = FuncionarioRepository()

    def exibir(self):
        while True:
            print()
            print("-" * 60)
            print("METALSUL - SISTEMA DE GERENCIAMENTO")
            print("-" * 60)
            print("1. Cadastrar Funcionário")
            print("2. Buscar Funcionário")
            print("3. Listar Funcionários")
            print("4. Atualizar Funcionário")
            print("5. Excluir Funcionário")
            print("0. Sair")
            print("-" * 60)

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

        try:
            salario = float(input("Salário: "))
        except ValueError:
            print("Valor de salário inválido.")
            input("\nPressione ENTER para continuar...")
            return

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
        print()
        print("=" * 60)
        print("BUSCAR FUNCIONÁRIO")
        print("=" * 60)

        try:
            id_funcionario = int(input("Código do funcionário: "))
        except ValueError:
            print("Código inválido.")
            input("\nPressione ENTER para continuar...")
            return

        funcionario = self.repository.buscar_por_id(id_funcionario)
        print()

        if funcionario is None:
            print("Funcionário não encontrado.")
        else:
            print(f"Código..........: {funcionario.id_funcionario}")
            print(f"Nome............: {funcionario.nome}")
            print(f"CPF.............: {funcionario.cpf}")
            print(f"RG..............: {funcionario.rg}")
            print(f"Nascimento......: {funcionario.data_nascimento}")
            print(f"Sexo............: {funcionario.sexo}")
            print(f"Estado Civil....: {funcionario.estado_civil}")
            print(f"E-mail..........: {funcionario.email}")
            print(f"Telefone........: {funcionario.telefone}")
            print(f"Celular.........: {funcionario.celular}")
            print(f"Cargo...........: {funcionario.cargo}")
            print(f"Departamento....: {funcionario.departamento}")
            print(f"Salário.........: R$ {funcionario.salario:.2f}")
            print(f"Admissão........: {funcionario.data_admissao}")
            print(f"Demissão........: {funcionario.data_demissao}")
            print(f"Turno...........: {funcionario.turno}")
            print(f"Status..........: {funcionario.status}")
            print(f"Observações.....: {funcionario.observacoes}")

        print()
        input("Pressione ENTER para continuar...")

    def listar_funcionarios(self):

        print()
        print("=" * 100)
        print("LISTA DE FUNCIONÁRIOS")
        print("=" * 100)

        funcionarios = self.repository.listar()

        if not funcionarios:
            print()
            print("Nenhum funcionário cadastrado.")
            print()
            input("Pressione ENTER para continuar...")
            return

        print(
            f"{'ID':<5}"
            f"{'Nome':<30}"
            f"{'Cargo':<25}"
            f"{'Departamento':<20}"
            f"{'Salário':>12}"
            f"{'Status':>12}"
        )
        print("-" * 110)

        for funcionario in funcionarios:
            print(
                f"{funcionario.id_funcionario:<5}"
                f"{funcionario.nome:<30}"
                f"{funcionario.cargo:<25}"
                f"{funcionario.departamento:<20}"
                f"{funcionario.salario:>12.2f}"
                f"{funcionario.status:>12}"
            )
        print()
        print(f"Total de funcionários: {len(funcionarios)}")
        print()
        input("Pressione ENTER para continuar...")

    def atualizar_funcionario(self):
        print()
        print("=" * 60)
        print("ATUALIZAÇÃO DE FUNCIONÁRIO")
        print("=" * 60)

        try:
            id_funcionario = int(
                input("Código do funcionário: ")
            )

        except ValueError:
            print()
            print("Código inválido.")
            input("\nPressione ENTER para continuar...")
            return

        funcionario = self.repository.buscar_por_id(
            id_funcionario
        )

        if funcionario is None:
            print()
            print("Funcionário não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        print()
        print("Pressione ENTER para manter o valor atual.")
        print()

        nome = input(
            f"Nome [{funcionario.nome}]: "
        )

        if nome:
            funcionario.nome = nome
        email = input(
            f"E-mail [{funcionario.email}]: "
        )

        if email:
            funcionario.email = email
        telefone = input(
            f"Telefone [{funcionario.telefone}]: "
        )

        if telefone:
            funcionario.telefone = telefone

        celular = input(
            f"Celular [{funcionario.celular}]: "

        )
        if celular:
            funcionario.celular = celular

        cargo = input(
            f"Cargo [{funcionario.cargo}]: "
        )

        if cargo:
            funcionario.cargo = cargo

        departamento = input(
            f"Departamento [{funcionario.departamento}]: "
        )

        if departamento:
            funcionario.departamento = departamento

        salario = input(
            f"Salário [{funcionario.salario}]: "
        )

        if salario:
            funcionario.salario = float(salario)

        turno = input(
            f"Turno [{funcionario.turno}]: "
        )

        if turno:
            funcionario.turno = turno

        status = input(
            f"Status [{funcionario.status}]: "
        )

        if status:
            funcionario.status = status

        observacoes = input(
            f"Observações [{funcionario.observacoes}]: "
        )

        if observacoes:
            funcionario.observacoes = observacoes

        self.repository.atualizar(funcionario)
        print()
        input("Pressione ENTER para continuar...")

    def excluir_funcionario(self):

        print()
        print("=" * 60)
        print("EXCLUSÃO DE FUNCIONÁRIO")
        print("=" * 60)

        try:
            id_funcionario = int(
                input("Código do funcionário: ")
            )

        except ValueError:
            print()
            print("Código inválido.")
            input("\nPressione ENTER para continuar...")
            return

        funcionario = self.repository.buscar_por_id(
            id_funcionario
        )

        if funcionario is None:
            print()
            print("Funcionário não encontrado.")
            input("\nPressione ENTER para continuar...")
            return

        print()
        print("Funcionário localizado")
        print("-" * 60)
        print(f"Código.......: {funcionario.id_funcionario}")
        print(f"Nome.........: {funcionario.nome}")
        print(f"Cargo........: {funcionario.cargo}")
        print(f"Departamento.: {funcionario.departamento}")
        print()

        resposta = input(
            "Deseja realmente excluir este funcionário? (S/N): "
        ).strip().upper()

        if resposta != "S":
            print()
            print("Operação cancelada.")
            input("\nPressione ENTER para continuar...")
            return

        self.repository.excluir(id_funcionario)
        print()
        input("Pressione ENTER para continuar...")