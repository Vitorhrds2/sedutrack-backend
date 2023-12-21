from flask import Blueprint, jsonify, request, current_app
from .modelo_service import ModeloService

class ModeloController:
    def __init__(self, app=None):
        self.service = ModeloService()
        self.bp = Blueprint('modelo_controller', __name__)
        self.app = app  # Atribui o objeto app ao atributo

        self.bp.route('/predict', methods=['POST'])(self.get_prediction)

    def get_prediction(self, *args, **kwargs):
        modelo_data = request.json

        if self.app:
            self.app.logger.info(f"Received prediction request with data: {modelo_data}")

        prediction = self.service.get_model_prediction(modelo_data)

        if self.app:
            self.app.logger.info(f"Prediction result: {prediction}")

        return jsonify(prediction)
