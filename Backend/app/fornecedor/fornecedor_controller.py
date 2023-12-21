from flask import Blueprint, jsonify, request
from .fornecedor_service import FornecedorService

class FornecedorController:
    def __init__(self):
        self.service = FornecedorService()
        self.bp = Blueprint('fornecedor_controller', __name__)

        self.bp.route('/fornecedor', methods=['POST'])(self.add_fornecedor)
        self.bp.route('/fornecedores', methods=['GET'])(self.get_fornecedors)
        self.bp.route('/fornecedor/<string:cnpj>', methods=['GET'])(self.get_fornecedor_by_cnpj)
        self.bp.route('/fornecedor', methods=['PATCH'])(self.update_fornecedor)
        self.bp.route('/fornecedor/<string:cnpj>', methods=['DELETE'])(self.delete_tranportadora)
    
    def add_fornecedor(self):
        fornecedor_data = request.json
        retorno = self.service.add_fornecedor(fornecedor_data)
        if retorno == True:
            return jsonify({"message": "Fornecedor adicionada com sucesso!"}), 201
        else:
            return jsonify({"message": "Fornecedor já cadastrada!"}), 409

    def get_fornecedors(self):
        return self.service.get_all_fornecedors()
    
    def get_fornecedor_by_cnpj(self, cnpj):
        fornecedor_cnpj = cnpj
        return self.service.get_fornecedor_by_cnpj(fornecedor_cnpj)
    
    def update_fornecedor(self):
        fornecedor_data = request.json
        retorno = self.service.update_fornecedor(fornecedor_data)
        if retorno == None:
            return jsonify({"message": "Fornecedor não encontrada!"}), 400
        else:
            return jsonify({"message": "fornecedor updated successfully"}), 201
    
    def delete_tranportadora(self, cnpj):
        fornecedor_cnpj = cnpj
        retorno = self.service.delete_fornecedor(fornecedor_cnpj)
        if retorno == True:
            return jsonify({"message": "Fornecedor deletada com sucesso!"}), 201
        else:
            return jsonify({"message": "Fornecedor não encontrada!"}), 201