from flask_testing import TestCase
from extensions import db
from app import create_app

class TestAvaliacao(TestCase):
    avaliationRange = range(0, 6)

    def create_app(self):
        app = create_app()
        return app

    def test_get_avaliacoes(self):  
        response = self.client.get("/avaliacoes")
        self.assertEqual(response.status_code, 200)

        # Verificar se a resposta JSON é uma lista
        self.assertIsInstance(response.json, list)

        # Verificar se cada avaliacao na lista tem os campos 'nota_fiscal_entrega', 'avaliacao_entregador', 'avaliacao_embalagem', 'avaliacao_materiais', 'avaliacao_pontualidade' e 'feedback'
        for avaliacao in response.json:
            self.assertIn('nota_fiscal_entrega', avaliacao)
            self.assertIn('avaliacao_entregador', avaliacao)
            self.assertIn('avaliacao_embalagem', avaliacao)
            self.assertIn('avaliacao_materiais', avaliacao)
            self.assertIn('avaliacao_pontualidade', avaliacao)
            self.assertIn('feedback', avaliacao)

            # Verificar se 'nota_fiscal_entrega', 'avaliacao_entregador', 'avaliacao_embalagem', 'avaliacao_materiais', 'avaliacao_pontualidade' e 'feedback' tem os tipos corretos
            self.assertIsInstance(avaliacao['nota_fiscal_entrega'], str)
            self.assertIsInstance(avaliacao['avaliacao_entregador'], str)
            self.assertIsInstance(avaliacao['avaliacao_embalagem'], str)
            self.assertIsInstance(avaliacao['avaliacao_materiais'], str)
            self.assertIsInstance(avaliacao['avaliacao_pontualidade'], str)
            self.assertIsInstance(avaliacao['feedback'], str)

            # check if the avaliation is in the range
            self.assertIn(int(avaliacao['avaliacao_entregador']), self.avaliationRange)
            self.assertIn(int(avaliacao['avaliacao_embalagem']), self.avaliationRange)
            self.assertIn(int(avaliacao['avaliacao_materiais']), self.avaliationRange)
            self.assertIn(int(avaliacao['avaliacao_pontualidade']), self.avaliationRange)


    def test_get_avaliacao_by_n_nota_fiscal(self):
        response = self.client.get("/avaliacao/1")
        self.assertEqual(response.status_code, 200)

        # Verifica se a resposta e um dicionario
        self.assertIsInstance(response.json, dict)

    def test_type_API(self):
        response = self.client.get("/avaliacao/1")
        self.assertEqual(response.status_code, 200)
        dados = response.json
        #print(dados)
        avaliacao_entregador = dados['avaliacao_entregador']
        avaliacao_embalagem = dados['avaliacao_embalagem']
        avaliacao_materiais = dados['avaliacao_materiais']
        avaliacao_pontualidade = dados['avaliacao_pontualidade']
        feedback = dados['feedback']

        # Verifica se as typegens estao corretas (strings)
        self.assertIsInstance(avaliacao_entregador, str)
        self.assertIsInstance(avaliacao_embalagem, str)
        self.assertIsInstance(avaliacao_materiais, str)
        self.assertIsInstance(avaliacao_pontualidade, str)
        self.assertIsInstance(feedback, str) 

        # Verifica se as avaliacoes estao no range
        self.assertIn(int(avaliacao_entregador), self.avaliationRange)
        self.assertIn(int(avaliacao_embalagem), self.avaliationRange)
        self.assertIn(int(avaliacao_materiais), self.avaliationRange)
        self.assertIn(int(avaliacao_pontualidade), self.avaliationRange)
       