class FuncionarioRepository:
    def __init__(self, db):
        self.db = db

    def get_all_funcionarios(self):
        return self.db.query(Funcionario).all()

    def get_funcionario_by_id(self, funcionario_id):
        return self.db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()

    def create_funcionario(self, funcionario_data):
        new_funcionario = Funcionario(**funcionario_data)
        self.db.add(new_funcionario)
        self.db.commit()
        self.db.refresh(new_funcionario)
        return new_funcionario

    def update_funcionario(self, funcionario_id, funcionario_data):
        funcionario = self.get_funcionario_by_id(funcionario_id)
        if funcionario:
            for key, value in funcionario_data.items():
                setattr(funcionario, key, value)
            self.db.commit()
            self.db.refresh(funcionario)
            return funcionario
        return None

    def delete_funcionario(self, funcionario_id):
        funcionario = self.get_funcionario_by_id(funcionario_id)
        if funcionario:
            self.db.delete(funcionario)
            self.db.commit()
            return True
        return False