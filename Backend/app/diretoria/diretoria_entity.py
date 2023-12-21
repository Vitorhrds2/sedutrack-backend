from extensions import db

class Diretoria(db.Model):
    nome = db.Column(db.String(255), primary_key=True)
    regiao = db.Column(db.String(255))
    escolas = db.relationship('Escola', back_populates='diretoria')

class Escola(db.Model):
    cie = db.Column(db.String(255), primary_key=True)
    nome_diretoria = db.Column(db.String(255), db.ForeignKey('diretoria.nome'))
    nome = db.Column(db.String(255))
    endereco = db.Column(db.String(255))
    numero = db.Column(db.String(255))
    bairro = db.Column(db.String(255))
    cep = db.Column(db.String(255))
    diretoria = db.relationship('Diretoria', back_populates='escolas')
    entregas_relacionadas = db.relationship('Entrega', back_populates='escola')

    def to_dict(self):
        return {
            'cie': self.cie,
            'nome_diretoria': self.nome_diretoria,
            'nome': self.nome,
            'endereco': self.endereco,
            'numero': self.numero,
            'bairro': self.bairro,
            'cep': self.cep
    }

