from .diretoria_repository import DiretoriaRepository
from .diretoria_entity import Diretoria

class DiretoriaService:
    def __init__(self):
        self.repository = DiretoriaRepository()

    def get_all_diretorias(self):
        diretorias = self.repository.get_all()
        return [self.to_dict(diretoria) for diretoria in diretorias]
    
    def get_diretoria_by_name(self, nome_diretoria):
        diretoria = self.repository.get_by_name(nome_diretoria)
        return self.to_dict(diretoria) if diretoria else None

    def get_escola_by_cie_escola(self, cie_escola):
        escola = self.repository.get_escola_by_cie_escola(cie_escola)
        return self.to_dict_escola(escola)

    def to_dict(self, diretoria):
        return{
            'nome': diretoria.nome,
            'regiao': diretoria.regiao,
            'escolas': [self.to_dict_escola(escola) for escola in diretoria.escolas]
        }
    
    def create_diretoria(self, diretoria):
        new_diretoria = Diretoria(**diretoria)
        self.repository.create(new_diretoria)
        return {"message": "Diretoria criada com sucesso!"}
    
    def add_escola(self, escola, diretoria):
        self.repository.add_escola(escola, diretoria)
        return {"message": "Escola adicionada com sucesso!"}

    def to_dict_escola(self, escola):
        return {
            'cie': escola.cie,
            'nome_diretoria': escola.nome_diretoria,
            'nome': escola.nome,
            'endereco': escola.endereco,
            'numero': escola.numero,
            'bairro': escola.bairro,
            'cep': escola.cep
    }