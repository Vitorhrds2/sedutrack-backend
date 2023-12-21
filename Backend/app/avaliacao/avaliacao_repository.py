from .avaliacao_entity import Avaliacao, db
from ..entrega.entrega_entity import Entrega
from ..entrega.entrega_repository import EntregaRepository

class AvaliacaoRepository:
    def __init__(self):
        self.db = db
        self.entrega_repository = EntregaRepository()

    def get_all(self):
        avaliacoes = Avaliacao.query.all()
        return avaliacoes
    
    def get_by_n_nota_fiscal(self, nota_fiscal_entrega):
        avaliacao = Avaliacao.query.filter_by(nota_fiscal_entrega=nota_fiscal_entrega).first()
        return avaliacao

    def add(self, avaliacao_data):
        nota_fiscal_entrega = avaliacao_data.get('nota_fiscal_entrega')
        cie_escola = self.entrega_repository.get_cie_escola_by_n_nota_fiscal(nota_fiscal_entrega)
        entrega_existente = Entrega.query.filter_by(n_nota_fiscal=avaliacao_data['nota_fiscal_entrega']).first()
        if entrega_existente: 
            new_avaliacao = Avaliacao(**avaliacao_data)


            # Adiciona e commita a nova avaliação
            db.session.add(new_avaliacao)
            db.session.commit()

            # Retorna um dicionário com a nota fiscal, o cie_escola e os dados da avaliação
            return {

                    'avaliacao_entregador': avaliacao_data['avaliacao_entregador'],
                    'avaliacao_embalagem': avaliacao_data['avaliacao_embalagem'],
                    'avaliacao_materiais': avaliacao_data['avaliacao_materiais'],
                    'avaliacao_pontualidade': avaliacao_data['avaliacao_pontualidade'],
                    'feedback': avaliacao_data['feedback'],
                    'cie_escola': cie_escola,
                
            }
        else: 
            return False
