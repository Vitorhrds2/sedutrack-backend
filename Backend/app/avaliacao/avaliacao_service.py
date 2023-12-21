from .avaliacao_repository import AvaliacaoRepository
from sendgrid.helpers.mail import Mail, Email, To, Content
import sendgrid

class AvaliacaoService:
    def __init__(self):
        self.repository = AvaliacaoRepository()

    def get_all_avaliacoes(self):
        avaliacoes = self.repository.get_all()
        return [self.to_dict(avaliacao) for avaliacao in avaliacoes]
    
    def get_by_n_nota_fiscal(self, nota_fiscal_entrega):
        avaliacao = self.repository.get_by_n_nota_fiscal(nota_fiscal_entrega)
        return self.to_dict(avaliacao)
    
    def add_avaliacao(self, avaliacao_data):
        cie_escola = self.repository.add(avaliacao_data)
        if cie_escola:
            return  cie_escola
        else:
            return False
    
    def enviar_email( self, sendgrid_client, from_email, to_email, subject, plain_text_content):
        mensagem = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            plain_text_content=plain_text_content
        )
        print('E-mail enviado com sucesso!')
        try:
            response = sendgrid_client.send(mensagem)
            mensagem = "E-mail enviado com sucesso"
            return response.status_code
        except Exception as e:
            print(e)
            return None

    def to_dict(self, avaliacao):
        return {
            'nota_fiscal_entrega': avaliacao.nota_fiscal_entrega,
            'avaliacao_entregador': avaliacao.avaliacao_entregador,
            'avaliacao_embalagem': avaliacao.avaliacao_embalagem,
            'avaliacao_materiais': avaliacao.avaliacao_materiais,
            'avaliacao_pontualidade': avaliacao.avaliacao_pontualidade,
            'feedback': avaliacao.feedback,
        }
