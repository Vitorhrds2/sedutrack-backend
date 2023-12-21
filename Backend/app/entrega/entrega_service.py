from .entrega_repository import EntregaRepository
from .entrega_entity import Entrega
import random

class EntregaService:
    def __init__(self):
        self.repository = EntregaRepository()

    def gerar_codigo_unico(self):
        while True:
            codigo = '{:04d}'.format(random.randint(0, 9999))
            if not Entrega.query.filter_by(codigo_unico=codigo).first():
                return codigo

    def get_all_entregas(self):
        entregas = self.repository.get_all()
        return [self.to_dict(entrega) for entrega in entregas]
    
    def get_entregas_por_cie_escola(self, cie_escola):
        entregas = self.repository.get_entregas_por_cie_escola(cie_escola)
        return [self.to_dict(entrega) for entrega in entregas]

    def get_entregas_por_cnpj_transportadora(self, cnpj_transportadora):
        entregas_cnpj_transportadora = self.repository.get_entregas_por_cnpj_transportadora(cnpj_transportadora)
        return [self.to_dict(entrega) for entrega in entregas_cnpj_transportadora]

    def get_entregas_por_cnpj_fornecedor(self, cnpj_fornecedor):
        entregas_cnpj_fornecedor = self.repository.get_entregas_por_cnpj_fornecedor(cnpj_fornecedor)
        return [self.to_dict(entrega) for entrega in entregas_cnpj_fornecedor]

    def add_entrega(self, entrega_data):
        entrega = Entrega(**entrega_data)
        try:
            entrega.validar_dados()
            entrega.codigo_unico = self.gerar_codigo_unico() 
            self.repository.add(entrega)
        except ValueError as e:
            return {"erros": e.args[0]}
        return {"message": "Entrega criada com sucesso!", "codigo_unico": entrega.codigo_unico}
        
    def get_por_n_nota_fiscal(self, nota_fiscal_entrega):
        entrega = self.repository.get_por_n_nota_fiscal(nota_fiscal_entrega)
        return self.to_dict(entrega)
    
    def atualiza_status_entrega(self, nota_fiscal_entrega, status_atualizado, data_inicio_entrega=None):
        self.repository.atualiza_status_entrega(nota_fiscal_entrega, status_atualizado, data_inicio_entrega)
        return {"message": "Status da entrega atualizado com sucesso"}
    
    def buscar_entregas_por_diretoria(self, nome_diretoria):
        entregas = self.repository.buscar_entregas_por_diretoria(nome_diretoria)
        return [entrega.to_dict() for entrega in entregas] 


    def to_dict(self, entrega):
        return {
            'n_nota_fiscal': entrega.n_nota_fiscal,
            'cnpj_fornecedor': entrega.cnpj_fornecedor,
            'cnpj_transportadora': entrega.cnpj_transportadora,
            'cie_escola': entrega.cie_escola,
            'gpb_ger': entrega.gpb_ger,
            'data_estimada_inicio': entrega.data_estimada_inicio,
            'data_estimada_fim': entrega.data_estimada_fim,
            'status_entrega': entrega.status_entrega,
            'email_usuario_transportadora': entrega.email_usuario_transportadora,
            'email_usuario_escola': entrega.email_usuario_escola,
            'data_entregue': entrega.data_entregue,
            'prova_entrega': entrega.prova_entrega,
            'data_criacao': entrega.data_criacao,
            'placa': entrega.placa,
            'valor': entrega.valor,
            'codigo_unico': entrega.codigo_unico,
            'data_inicio_entrega': entrega.data_inicio_entrega
        }