from flask import Blueprint, jsonify, request
from .modelo_service import ModeloService

class ModeloController:
    def __init__(self):
        self.service = ModeloService()
        self.bp = Blueprint('modelo_controller', __name__)

        self.bp.route('/predict', methods=['POST'])(self.get_prediction)

    def get_prediction(self):
        modelo_data = request.json

        prediction = self.service.get_model_prediction(modelo_data)
        return jsonify(prediction)