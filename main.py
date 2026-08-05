from datetime import date
from models.funcionario import Funcionario


def main():
    funcionario = Funcionario(
        nome="João da Silva",
        cpf="123.456.789-00",
        cargo="Analista de Sistemas",
        departamento="TI",
        salario=5000.00,
        status="ATIVO",
        data_admissao=date.today()
    )
    print(funcionario)

if __name__ == "__main__":
    main()    