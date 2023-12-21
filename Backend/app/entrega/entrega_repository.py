from .entrega_entity import Entrega, db
from ..diretoria.diretoria_entity import Escola, Diretoria
from sqlalchemy import update
from sqlalchemy.orm import joinedload

class EntregaRepository:
    def __init__(self):
        self.db = db

    def get_all(self):
        entregas = Entrega.query.all()
        return entregas
    
    def get_entregas_por_cie_escola(self, cie_escola):
        entregas_concluida = Entrega.query.filter_by(cie_escola = cie_escola)
        return entregas_concluida

    def get_entregas_por_cnpj_transportadora(self, cnpj_transportadora):
        entregas_transportadora = Entrega.query.filter_by(cnpj_transportadora=cnpj_transportadora).filter(Entrega.status_entrega == 'Pendente')
        return entregas_transportadora

    def get_entregas_por_cnpj_fornecedor(self, cnpj_fornecedor):
        entregas_fornecedor = Entrega.query.filter_by(cnpj_fornecedor=cnpj_fornecedor).filter(Entrega.status_entrega != 'Concluida')
        return entregas_fornecedor
    
    def get_cie_escola_by_n_nota_fiscal(self, n_nota_fiscal):
        entrega = Entrega.query.filter_by(n_nota_fiscal=n_nota_fiscal).first()
        if entrega:
            return entrega.cie_escola
        else:
            return None

    def add(self, entrega):
        db.session.add(entrega)
        db.session.commit()
        return True
        
    def get_por_n_nota_fiscal(self, nota_fiscal_entrega):
        entrega = Entrega.query.filter_by(n_nota_fiscal=nota_fiscal_entrega).first()
        return entrega
    
    def atualiza_status_entrega(self, nota_fiscal_entrega, status_atualizado, data_inicio_entrega=None):
        update_values = {Entrega.status_entrega: status_atualizado}
        print(update_values)
        if data_inicio_entrega and status_atualizado == 'Em andamento':
            update_values[Entrega.data_inicio_entrega] = data_inicio_entrega
        elif data_inicio_entrega and status_atualizado == 'Entregue':
            update_values[Entrega.data_entregue] = data_inicio_entrega


        db.session.execute(
            update(Entrega)
            .where(Entrega.n_nota_fiscal == nota_fiscal_entrega)
            .values(update_values)
        )
        db.session.commit()

    def buscar_entregas_por_diretoria(self, nome_diretoria):
        entregas = (db.session.query(Entrega)
                    .join(Entrega.escola)
                    .join(Escola.diretoria)
                    .filter(Diretoria.nome == nome_diretoria)
                    .options(joinedload(Entrega.escola))
                    .all())
        return entregas

