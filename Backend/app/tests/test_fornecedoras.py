from flask_testing import TestCase
from extensions import db
from app import create_app

class TestFornecedoras(TestCase):
    def create_app(self):
        app = create_app()
        return app
    
    def test_get_fornecedors(self):
        response = self.client.get("/fornecedores")

        self.assertEqual(response.status_code, 200)

        # Verificar se a resposta JSON é uma lista
        self.assertIsInstance(response.json, list)

        # Verificar se cada fornecedor na lista tem os campos 'nome', 'cnpj'
        for fornecedor in response.json:
            self.assertIn('nome', fornecedor)
            self.assertIn('cnpj', fornecedor)

            # Verificar se 'nome', 'cnpj' tem os tipos corretos
            self.assertIsInstance(fornecedor['nome'], str)
            self.assertIsInstance(fornecedor['cnpj'], str)
        
    def test_get_fornecedor_by_cnpj(self):
        response = self.client.get("/fornecedor/00.369.6460001-40")
        self.assertEqual(response.status_code, 200)

        # Verifica se a resposta e um dicionario
        self.assertIsInstance(response.json, dict)

    def test_type_API(self):
        response = self.client.get("/fornecedor/00.369.6460001-40")
        self.assertEqual(response.status_code, 200)
        dados = response.json
        #print(dados)
        nome = dados['nome']
        cnpj = dados['cnpj']

        # Verifica se as typegens estao corretas (strings)
        self.assertIsInstance(nome, str)
        self.assertIsInstance(cnpj, str)
        