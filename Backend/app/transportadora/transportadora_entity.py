from extensions import db

class Transportadora(db.Model):
    cnpj = db.Column(db.String(255), primary_key=True)
    nome = db.Column(db.String(255))
    logradouro = db.Column(db.String(255))
    numero = db.Column(db.String(255))
    bairro = db.Column(db.String(255))
    cep = db.Column(db.String(255))
    entregas = db.relationship('Entrega', backref='transportadora', lazy='subquery')

    # def __repr__(self):
    #     return '<Transportadora %r>' % self.cnpj