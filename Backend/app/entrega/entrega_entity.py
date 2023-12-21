from extensions import db

class Entrega(db.Model):
    from ..fornecedor.fornecedor_entity import Fornecedor
    from ..transportadora.transportadora_entity import Transportadora
    n_nota_fiscal = db.Column(db.String(255), primary_key=True)
    cnpj_fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.cnpj'), nullable=False)
    cnpj_transportadora = db.Column(db.String(255), db.ForeignKey('transportadora.cnpj'), nullable=False)
    cie_escola = db.Column(db.Integer, db.ForeignKey('escola.cie'), nullable=False)
    gpb_ger = db.Column(db.String(255), nullable=False)
    data_estimada_inicio = db.Column(db.DateTime, nullable=False)
    data_estimada_fim = db.Column(db.DateTime, nullable=False)
    status_entrega = db.Column(db.String(255), nullable=False)
    email_usuario_transportadora = db.Column(db.String(255), nullable=False)
    email_usuario_escola = db.Column(db.String(255), nullable=False)
    data_entregue = db.Column(db.DateTime)
    prova_entrega = db.Column(db.Boolean)
    data_criacao = db.Column(db.DateTime)
    data_inicio_entrega = db.Column(db.DateTime)
    placa = db.Column(db.String(20), nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    escola = db.relationship('Escola', back_populates='entregas_relacionadas')
    codigo_unico = db.Column(db.String(4), nullable=False, unique=True)

    def validar_dados(self):
        erros = {}
        if not self.n_nota_fiscal:
            erros["n_nota_fiscal"] = "Nota fiscal é obrigatória."
        if not self.cnpj_fornecedor:
            erros["cnpj_fornecedor"] = "CNPJ do fornecedor é obrigatório."
        if not self.cnpj_transportadora:
            erros["cnpj_transportadora"] = "CNPJ da transportadora é obrigatório."
        if not self.cie_escola:
            erros["cie_escola"] = "CIE da escola é obrigatório."
        if not self.gpb_ger:
            erros["gpb_ger"] = "GPB GER é obrigatório."
        if not self.data_estimada_inicio:
            erros["data_estimada_inicio"] = "Data estimada de início é obrigatória."
        if not self.data_estimada_fim:
            erros["data_estimada_fim"] = "Data estimada de fim é obrigatória."
        if not self.status_entrega:
            erros["status_entrega"] = "Status da entrega é obrigatório."
        if not self.email_usuario_transportadora:
            erros["email_usuario_transportadora"] = "E-mail do usuário da transportadora é obrigatório."
        if not self.email_usuario_escola:
            erros["email_usuario_escola"] = "E-mail do usuário da escola é obrigatório."
        if self.prova_entrega is None:
            erros["prova_entrega"] = "Prova de entrega é obrigatória."
        if not self.placa:
            erros["placa"] = "Placa é obrigatória."
        if self.valor is None or self.valor <= 0:  # Assumindo que o valor deve ser positivo
            erros["valor"] = "Valor é obrigatório e deve ser maior que zero."

        if erros:
            raise ValueError(erros)
        
    def to_dict(self):
        return {
            'n_nota_fiscal': self.n_nota_fiscal,
            'cnpj_fornecedor': self.cnpj_fornecedor,
            'cnpj_transportadora': self.cnpj_transportadora,
            'cie_escola': self.cie_escola,
            'gpb_ger': self.gpb_ger,
            'data_estimada_inicio': self.data_estimada_inicio.isoformat() if self.data_estimada_inicio else None,
            'data_estimada_fim': self.data_estimada_fim.isoformat() if self.data_estimada_fim else None,
            'status_entrega': self.status_entrega,
            'email_usuario_transportadora': self.email_usuario_transportadora,
            'email_usuario_escola': self.email_usuario_escola,
            'data_entregue': self.data_entregue.isoformat() if self.data_entregue else None,
            'prova_entrega': self.prova_entrega,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'placa': self.placa,
            'valor': self.valor
    }