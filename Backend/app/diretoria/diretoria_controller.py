from flask import Blueprint, jsonify, request
from .diretoria_service import DiretoriaService

class DiretoriaController:
    def __init__(self):
        self.service = DiretoriaService()
        self.bp = Blueprint('diretoria_controller', __name__)

        self.bp.route('/diretorias', methods = ['GET'])(self.get_diretorias)
        self.bp.route('/diretoria/<string:nome_diretoria>', methods = ['GET'])(self.get_diretoria_by_name)
        self.bp.route('/diretoria', methods = ['POST'])(self.create_diretoria)
        self.bp.route('/diretoria/<string:diretoria>/escola', methods = ['POST'])(self.add_escola)
        self.bp.route('/escola/<string:cie_escola>', methods = ['GET'])(self.get_escola_by_cie_escola)

    def get_diretorias(self):
        diretorias = self.service.get_all_diretorias()
        return jsonify(diretorias), 200
    
    def get_diretoria_by_name(self, nome_diretoria):
        diretoria = self.service.get_diretoria_by_name(nome_diretoria)
        return jsonify(diretoria), 200

    def get_escola_by_cie_escola(self, cie_escola):
        escola = self.service.get_escola_by_cie_escola(cie_escola)
        return jsonify(escola), 200
        
    
    def create_diretoria(self):
        diretoria = request.json
        diretoria = self.service.create_diretoria(diretoria)
        return jsonify(diretoria), 201

    def add_escola(self, diretoria):
        escola = request.json
        escola = self.service.add_escola(escola, diretoria)
        return jsonify(escola), 201