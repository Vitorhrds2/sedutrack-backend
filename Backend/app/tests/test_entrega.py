from flask_testing import TestCase
from extensions import db
from app import create_app

class TestEntregas(TestCase):
    def create_app(self):
        app = create_app()
        return app

    def test_get_entregas(self):    
        response = self.client.get("/entregas")
        self.assertEqual(response.status_code, 200)

        # Verificar se a resposta JSON é uma lista
        self.assertIsInstance(response.json, list)

        # Verificar se cada entrega na lista tem os campos 'n_nota_fiscal', 'cnpj_fornecedor', 'cnpj_transportadora', 'cie_escola', 'gpb_ger', 'data_estimada_inicio', 'data_estimada_fim', 'status_entrega', 'email_usuario_transportadora', 'email_usuario_escola', 'data_entregue', 'prova_entrega', 'data_criacao', 'placa' e 'valor'
        for entrega in response.json:
            self.assertIn('n_nota_fiscal', entrega)
            self.assertIn('cnpj_fornecedor', entrega)
            self.assertIn('cnpj_transportadora', entrega)
            self.assertIn('cie_escola', entrega)
            self.assertIn('gpb_ger', entrega)
            self.assertIn('data_estimada_inicio', entrega)
            self.assertIn('data_estimada_fim', entrega)
            self.assertIn('status_entrega', entrega)
            self.assertIn('email_usuario_transportadora', entrega)
            self.assertIn('email_usuario_escola', entrega)
            self.assertIn('data_entregue', entrega)
            self.assertIn('prova_entrega', entrega)
            self.assertIn('data_criacao', entrega)
            self.assertIn('placa', entrega)
            self.assertIn('valor', entrega)

            # Verificar se 'n_nota_fiscal', 'cnpj_fornecedor', 'cnpj_transportadora', 'cie_escola', 'gpb_ger', 'data_estimada_inicio', 'data_estimada_fim', 'status_entrega', 'email_usuario_transportadora', 'email_usuario_escola', 'data_entregue', 'prova_entrega', 'data_criacao', 'placa' e 'valor' tem os tipos corretos
            self.assertIsInstance(entrega['n_nota_fiscal'], str)
            self.assertIsInstance(entrega['cnpj_fornecedor'], str)
            self.assertIsInstance(entrega['cnpj_transportadora'], str)
            self.assertIsInstance(entrega['cie_escola'], str)
            self.assertIsInstance(entrega['gpb_ger'], str)
            self.assertIsInstance(entrega['data_estimada_inicio'], str)
            self.assertIsInstance(entrega['data_estimada_fim'], str)
            self.assertIsInstance(entrega['status_entrega'], str)
            self.assertIsInstance(entrega['email_usuario_transportadora'], str)
            self.assertIsInstance(entrega['email_usuario_escola'], str)
            self.assertIsInstance(entrega['data_entregue'], str)
            self.assertIsInstance(entrega['prova_entrega'], bool)
            self.assertIsInstance(entrega['data_criacao'], str)
            self.assertIsInstance(entrega['placa'], str)
            self.assertIsInstance(entrega['valor'], int)
            
    # error test
    def test_get_entrega_by_n_nota_fiscal_error(self):
        response = self.client.get("/entrega/jefferson")

        self.assertEqual(response.status_code, 500)




