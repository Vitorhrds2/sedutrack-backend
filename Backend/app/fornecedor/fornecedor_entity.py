from extensions import db 

class Fornecedor(db.Model):
    nome = db.Column(db.String(255))
    cnpj = db.Column(db.String(255), primary_key=True)
    entregas = db.relationship('Entrega', backref='fornecedor', lazy=True)