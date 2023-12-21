from .fornecedor_entity import Fornecedor, db
from sqlalchemy.exc import IntegrityError

class FornecedorRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        fornecedores = Fornecedor.query.all()
        return fornecedores

    def add(self, fornecedor_data):
        try:
            fornecedor = Fornecedor(
                cnpj=fornecedor_data['cnpj'],
                nome=fornecedor_data['nome']
            )
            db.session.add(fornecedor)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def get_by_cnpj(self, cnpj):
        fornecedor = Fornecedor.query.filter_by(cnpj=cnpj).first()
        return fornecedor

    def update(self, fornecedor_data):
        fornecedor = Fornecedor.query.filter_by(cnpj=fornecedor_data['cnpj']).first()
        if fornecedor:
            fornecedor.nome = fornecedor_data['nome']
            db.session.commit()
            return True

    def delete(self, cnpj):
        fornecedor = Fornecedor.query.filter_by(cnpj=cnpj).first()
        if fornecedor:
            db.session.delete(fornecedor)
            db.session.commit()
            return True