from flask import Blueprint, jsonify, request
from .entrega_service import EntregaService

class EntregaController:
    def __init__(self):
        self.service = EntregaService()
        self.bp = Blueprint('entrega_controller', __name__)

        self.bp.route('/entregas', methods=['GET'])(self.get_entregas)
        self.bp.route('/entregas/status/<string:cie_escola>', methods = ['GET'])(self.get_entregas_por_cie_escola)
        self.bp.route('/entrega', methods=['POST'])(self.add_entrega)
        self.bp.route('/entrega/<string:n_nota_fiscal>', methods=['GET'])(self.get_entrega_por_n_nota_fiscal)
        self.bp.route('/entrega/<string:nota_fiscal_entrega>/<string:status_atualizado>', methods=['PATCH'])(self.refresh_entrega)
        self.bp.route('/entregas/<string:diretoria>', methods=['GET'])(self.entregas_by_diretoria)
        self.bp.route('/entrega/transportadora/<string:cnpj_transportadora>', methods=['GET'])(self.get_entregas_por_cnpj_transportadora)
        self.bp.route('/entrega/fornecedor/<string:cnpj_fornecedor>', methods=['GET'])(self.get_entregas_por_cnpj_fornecedor)

        

    def get_entregas(self):
        entregas = self.service.get_all_entregas()
        return jsonify(entregas)
    
    def get_entregas_por_cie_escola(self, cie_escola):
        entregas_por_status = self.service.get_entregas_por_cie_escola(cie_escola)
        return jsonify(entregas_por_status)

    def get_entregas_por_cnpj_transportadora(self, cnpj_transportadora):
        entregas_transportadora = self.service.get_entregas_por_cnpj_transportadora(cnpj_transportadora)
        return jsonify(entregas_transportadora)

    def get_entregas_por_cnpj_fornecedor(self, cnpj_fornecedor):
        entregas_fornecedor = self.service.get_entregas_por_cnpj_fornecedor(cnpj_fornecedor)
        return jsonify(entregas_fornecedor)
    
    def add_entrega(self):
        entrega_data = request.json
        resultado = self.service.add_entrega(entrega_data)
        if "erros" in resultado:
            return jsonify(resultado), 400
        return jsonify(resultado), 201

    def get_entrega_por_n_nota_fiscal(self, n_nota_fiscal):
        entrega = self.service.get_por_n_nota_fiscal(n_nota_fiscal)
        return jsonify(entrega)
    
    def refresh_entrega(self, nota_fiscal_entrega, status_atualizado):
        entrega_data = request.json
        data_inicio = entrega_data.get('data_inicio_entrega') or entrega_data.get('data_entregue')
        entrega = self.service.atualiza_status_entrega(nota_fiscal_entrega, status_atualizado, data_inicio)
        return jsonify(entrega)
    
    def entregas_by_diretoria(self, diretoria):
        entregas = self.service.buscar_entregas_por_diretoria(diretoria)
        return jsonify(entregas) 