from flask_testing import TestCase
from extensions import db
from app import create_app

class TestDiretorias(TestCase):
    def create_app(self):
        app = create_app()
        return app

    def test_get_diretorias(self):
        response = self.client.get("/diretorias")
        self.assertEqual(response.status_code, 200)

        # Verificar se a resposta JSON é uma lista
        self.assertIsInstance(response.json, list)

        # Verificar se cada diretoria na lista tem os campos 'nome', 'regiao' e 'escolas'
        for diretoria in response.json:
            self.assertIn('nome', diretoria)
            self.assertIn('regiao', diretoria)
            self.assertIn('escolas', diretoria)

            # Verificar se 'escolas' é uma lista e tem os campos esperados
            for escola in diretoria['escolas']:
                self.assertIn('bairro', escola)
                self.assertIn('cep', escola)
                self.assertIn('cie', escola)
                self.assertIn('endereco', escola)
                self.assertIn('nome', escola)
                self.assertIn('nome_diretoria', escola)
                self.assertIn('numero', escola)
    
    def test_get_diretoria_by_name(self):
        response = self.client.get("/diretoria/Suzano")
        self.assertEqual(response.status_code, 200)

        # Verifica se a resposta e um dicionario
        self.assertIsInstance(response.json, dict)

    def test_type_API(self):
        response = self.client.get("/diretoria/Suzano")
        self.assertEqual(response.status_code, 200)
        dados = response.json
        #print(dados)
        for escola in dados['escolas']:
            bairro = escola['bairro']
            cep = escola['cep']
            cie = escola['cie']
            endereco = escola['endereco']
            nome = escola['nome']
            nome_diretoria = escola['nome_diretoria']
            numero = escola['numero']

        # Verifica se as typegens estao corretas (strings)
        self.assertIsInstance(bairro, str)
        self.assertIsInstance(cep, str)
        self.assertIsInstance(cie, str)
        self.assertIsInstance(endereco, str)
        self.assertIsInstance(nome, str)
        self.assertIsInstance(nome_diretoria, str)
        self.assertIsInstance(numero, str)