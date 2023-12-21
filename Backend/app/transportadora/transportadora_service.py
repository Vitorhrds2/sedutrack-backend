from .transportadora_repository import TransportadoraRepository

class TransportadoraService:
    def __init__(self) -> None:
        self.repository = TransportadoraRepository()
    
    def add_transportadora(self, transportadora_data):
        retorno = self.repository.add(transportadora_data)
        return retorno

    def get_all_transportadoras(self):
        transportadoras = self.repository.get_all()
        return [self.to_dict(transportadora) for transportadora in transportadoras]

    def get_transportadora_by_cnpj(self, cnpj):
        transportadora = self.repository.get_by_cnpj(cnpj)
        return self.to_dict(transportadora)

    def update_transportadora(self, transportadora_data):
        retorno = self.repository.update(transportadora_data)
        return retorno
        

    def delete_transportadora(self, cnpj):
        retorno = self.repository.delete(cnpj)
        return retorno

    def to_dict(self, transportadora):
        return {
            'cnpj': transportadora.cnpj,
            'nome': transportadora.nome,
            'logradouro': transportadora.logradouro,
            'numero': transportadora.numero,
            'bairro': transportadora.bairro,
            'cep': transportadora.cep,
        }
    


