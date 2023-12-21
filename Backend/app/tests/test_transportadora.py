from flask_testing import TestCase
from extensions import db
from app import create_app

class TestTransportadoras(TestCase):
    def create_app(self):
        app = create_app()
        return app
    
    def test_get_transportadoras(self):
            # cnpj = db.Column(db.String(255), primary_key=True)
            # nome = db.Column(db.String(255))
            # logradouro = db.Column(db.String(255))
            # numero = db.Column(db.String(255))
            # bairro = db.Column(db.String(255))
            # cep = db.Column(db.String(255))
        response = self.client.get("/transportadoras")

        self.assertEqual(response.status_code, 200)

        # Verificar se a resposta JSON é uma lista
        self.assertIsInstance(response.json, list)

        # Verificar se cada transportadora na lista tem os campos 'cnpj', 'nome', 'logradouro', 'numero', 'bairro', 'cep'

        for transportadora in response.json:
            self.assertIn('cnpj', transportadora)
            self.assertIn('nome', transportadora)
            self.assertIn('logradouro', transportadora)
            self.assertIn('numero', transportadora)
            self.assertIn('bairro', transportadora)
            self.assertIn('cep', transportadora)

            # Verificar se 'cnpj', 'nome', 'logradouro', 'numero', 'bairro', 'cep' tem os tipos corretos
            self.assertIsInstance(transportadora['cnpj'], str)
            self.assertIsInstance(transportadora['nome'], str)
            self.assertIsInstance(transportadora['logradouro'], str)
            self.assertIsInstance(transportadora['numero'], str)
            self.assertIsInstance(transportadora['bairro'], str)
            self.assertIsInstance(transportadora['cep'], str)
