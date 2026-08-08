from database.conexao import Conexao
from models.funcionario import Funcionario


class FuncionarioRepository:
    def __init__(self):
        self.db = Conexao()

    def salvar(self, funcionario):
        sql = """
            INSERT INTO funcionario (
                nome, cpf, rg, data_nascimento, sexo, estado_civil,
                email, telefone, celular, cargo, departamento, salario,
                data_admissao, data_demissao, turno, status, observacoes
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        valores = (
            funcionario.nome,
            funcionario.cpf,
            funcionario.rg,
            funcionario.data_nascimento,
            funcionario.sexo,
            funcionario.estado_civil,
            funcionario.email,
            funcionario.telefone,
            funcionario.celular,
            funcionario.cargo,
            funcionario.departamento,
            funcionario.salario,
            funcionario.data_admissao,
            funcionario.data_demissao,
            funcionario.turno,
            funcionario.status,
            funcionario.observacoes,
        )
        #bloco de tratamento de erros
        try:
            self.db.cursor.execute(sql, valores)
            self.db.commit()
            print("Funcionário salvo com sucesso!")
        except Exception as erro:
            self.db.rollback()
            print(f"Erro ao salvar funcionário: {erro}")

    def buscar_por_id(self, id_funcionario):

        sql = """

            SELECT *

            FROM funcionario

            WHERE id_funcionario = %s

        """

        try:

            self.db.cursor.execute(sql, (id_funcionario,))

            registro = self.db.cursor.fetchone()

            if registro is None:

                return None

            funcionario = Funcionario(

                id_funcionario=registro[0],

                nome=registro[1],

                cpf=registro[2],

                rg=registro[3],

                data_nascimento=registro[4],

                sexo=registro[5],

                estado_civil=registro[6],

                email=registro[7],

                telefone=registro[8],

                celular=registro[9],

                cargo=registro[10],

                departamento=registro[11],

                salario=registro[12],

                data_admissao=registro[13],

                data_demissao=registro[14],

                turno=registro[15],

                status=registro[16],

                observacoes=registro[17]

            )

            return funcionario

        except Exception as erro:

            print(f"Erro ao buscar funcionário: {erro}")

            return None

    def listar(self):

        sql = """

            SELECT *

            FROM funcionario

            ORDER BY nome

        """

        try:

            self.db.cursor.execute(sql)

            registros = self.db.cursor.fetchall()

            funcionarios = []

            for registro in registros:

                funcionario = Funcionario(

                    id_funcionario=registro[0],

                    nome=registro[1],

                    cpf=registro[2],

                    rg=registro[3],

                    data_nascimento=registro[4],

                    sexo=registro[5],

                    estado_civil=registro[6],

                    email=registro[7],

                    telefone=registro[8],

                    celular=registro[9],

                    cargo=registro[10],

                    departamento=registro[11],

                    salario=registro[12],

                    data_admissao=registro[13],

                    data_demissao=registro[14],

                    turno=registro[15],

                    status=registro[16],

                    observacoes=registro[17]

                )

                funcionarios.append(funcionario)

            return funcionarios

        except Exception as erro:

            print(f"Erro ao listar funcionários: {erro}")

            return []

    def atualizar(self, funcionario):
        pass
    def excluir(self, id_funcionario):
        pass
    def fechar(self):
        self.db.fechar()