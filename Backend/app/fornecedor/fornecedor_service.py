from .fornecedor_repository import FornecedorRepository

class FornecedorService:
    def __init__(self) -> None:
        self.repository = FornecedorRepository()
    
    def add_fornecedor(self, fornecedor_data):
        retorno = self.repository.add(fornecedor_data)
        return retorno

    def get_all_fornecedors(self):
        fornecedors = self.repository.get_all()
        return [self.to_dict(fornecedor) for fornecedor in fornecedors]

    def get_fornecedor_by_cnpj(self, cnpj):
        fornecedor = self.repository.get_by_cnpj(cnpj)
        return self.to_dict(fornecedor)

    def update_fornecedor(self, fornecedor_data):
        retorno = self.repository.update(fornecedor_data)
        return retorno
        

    def delete_fornecedor(self, cnpj):
        retorno = self.repository.delete(cnpj)
        return retorno

    def to_dict(self, fornecedor):
        return {
            'nome': fornecedor.nome,
            'cnpj': fornecedor.cnpj,
        }