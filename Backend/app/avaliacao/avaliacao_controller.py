from flask import Blueprint, jsonify, request
from .avaliacao_service import AvaliacaoService
from sendgrid.helpers.mail import Mail, Email, To, Content
import sendgrid
import os
from dotenv import load_dotenv

load_dotenv()

sendgrid_client = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))


class AvaliacaoController:
    def __init__(self):
        self.service = AvaliacaoService()
        self.bp = Blueprint('avaliacao_controller', __name__)

        self.bp.route('/avaliacoes', methods=['GET'])(self.get_avaliacoes)
        self.bp.route('/avaliacao', methods=['POST'])(self.add_avaliacao)
        self.bp.route('/avaliacao/<n_nota_fiscal>', methods=['GET'])(self.get_avaliacao_by_n_nota_fiscal)

    def get_avaliacoes(self):
        avaliacoes = self.service.get_all_avaliacoes()
        return jsonify(avaliacoes)

    def get_avaliacao_by_n_nota_fiscal(self, n_nota_fiscal):
        avaliacao = self.service.get_by_n_nota_fiscal(n_nota_fiscal)
        return jsonify(avaliacao)

    def add_avaliacao(self):
        avaliacao_data = request.json
        adicionar_avaliacao = self.service.add_avaliacao(avaliacao_data)

        escola = "E.E. José Henrique de Paula e Silva"
        fornecedor = "JSL"
        from_email = "luiz.covas@sou.inteli.edu.br"
        to_email = "hrdsvitor@gmail.com"
        subject = "Entrega realizada!!"
        plain_text_content='Entrega de ' + fornecedor + ' para ' + escola + ' foi concluída!!'
        enviar_email = self.service.enviar_email(sendgrid_client, from_email, to_email, subject, plain_text_content)

        if enviar_email and adicionar_avaliacao:
            return jsonify({"message": "E-mail enviado com sucesso!" + "\nAvaliação feita com sucesso!"},
                           adicionar_avaliacao), 201
        else:
            return jsonify({"message": "Não foi possivel enviar o e-mail!" + "\nNão foi possivel fazer a avaliação. Nota fiscal não encontrada!"}), 404