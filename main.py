from datetime import date
from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository
from menu import Menu

def main():
    menu = Menu()
    menu.exibir()

if __name__ == "__main__":

    main()
