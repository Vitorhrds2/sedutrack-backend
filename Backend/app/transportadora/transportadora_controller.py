from flask import Blueprint, jsonify, request
from .transportadora_service import TransportadoraService

class TransportadoraController:
    def __init__(self):
        self.service = TransportadoraService()
        self.bp = Blueprint('transportadora_controller', __name__)

        self.bp.route('/transportadora', methods=['POST'])(self.add_transportadora)
        self.bp.route('/transportadoras', methods=['GET'])(self.get_transportadoras)
        self.bp.route('/transportadora/<string:cnpj>', methods=['GET'])(self.get_transportadora_by_cnpj)
        self.bp.route('/transportadora', methods=['PATCH'])(self.update_transportadora)
        self.bp.route('/transportadora/<string:cnpj>', methods=['DELETE'])(self.delete_tranportadora)
    
    def add_transportadora(self):
        transportadora_data = request.json
        retorno = self.service.add_transportadora(transportadora_data)
        if retorno == True:
            return jsonify({"message": "Transportadora adicionada com sucesso!"}), 201
        else:
            return jsonify({"message": "Transportadora já cadastrada!"}), 409

    def get_transportadoras(self):
        return self.service.get_all_transportadoras()
    
    def get_transportadora_by_cnpj(self, cnpj):
        transportadora_cnpj = cnpj
        return self.service.get_transportadora_by_cnpj(transportadora_cnpj)
    
    def update_transportadora(self):
        transportadora_data = request.json
        retorno = self.service.update_transportadora(transportadora_data)
        if retorno == None:
            return jsonify({"message": "Transportadora não encontrada!"}), 400
        else:
            return jsonify({"message": "transportadora updated successfully"}), 201
    
    def delete_tranportadora(self, cnpj):
        transportadora_cnpj = cnpj
        retorno = self.service.delete_transportadora(transportadora_cnpj)
        if retorno == True:
            return jsonify({"message": "Transportadora deletada com sucesso!"}), 201
        else:
            return jsonify({"message": "Transportadora não encontrada!"}), 201