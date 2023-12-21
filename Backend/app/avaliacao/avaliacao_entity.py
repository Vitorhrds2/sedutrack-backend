from extensions import db


class Avaliacao(db.Model):
    from ..entrega.entrega_entity import Entrega
    nota_fiscal_entrega = db.Column(db.String(255), db.ForeignKey(f'{Entrega.__tablename__}.n_nota_fiscal'), primary_key=True, nullable=False)
    avaliacao_entregador = db.Column(db.Integer)
    avaliacao_embalagem = db.Column(db.Integer)
    avaliacao_materiais = db.Column(db.Integer)
    avaliacao_pontualidade = db.Column(db.Integer)
    feedback = db.Column(db.String(255), nullable=True)

