from .diretoria_entity import Diretoria, Escola, db
from sqlalchemy.orm import joinedload

class DiretoriaRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        diretorias = Diretoria.query.all()
        return diretorias
    
    def get_by_name(self, nome_diretoria):
        diretoria = Diretoria.query.options(joinedload(Diretoria.escolas)).filter_by(nome=nome_diretoria).first()
        return diretoria

    def create(self, diretoria):
        self.db.session.add(diretoria)
        self.db.session.commit()
        return diretoria
    
    def add_escola(self, escola, diretoria):
        diretoria = Diretoria.query.filter_by(nome=diretoria).first()
        escola = Escola(cie=escola['cie'], nome=escola['nome'], endereco=escola['endereco'], numero=escola['numero'], bairro=escola['bairro'], cep=escola['cep'])
        diretoria.escolas.append(escola)
        self.db.session.add(diretoria)
        self.db.session.commit()
        return diretoria
    def get_escola_by_cie_escola(self, cie_escola):
        escola = Escola.query.filter_by(cie=cie_escola).first()
        return escola

