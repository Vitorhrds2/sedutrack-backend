from flask import Flask, render_template
from flask_cors import CORS
from extensions import db
from app.config.config import Config
from flasgger import Swagger
from app.entrega.entrega_controller import EntregaController
from app.diretoria.diretoria_controller import DiretoriaController
from app.avaliacao.avaliacao_controller import AvaliacaoController
from app.transportadora.transportadora_controller import TransportadoraController
from app.fornecedor.fornecedor_controller import FornecedorController
# from app.modelo.modelo_controller import ModeloController
from app.config.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Habilitar CORS
    CORS(app, origins='*')

    transportadora_controller = TransportadoraController()
    fornecedor_controller = FornecedorController()
    entrega_controller = EntregaController()
    diretoria_controller = DiretoriaController()
    avaliacoes_controller = AvaliacaoController()
    # modelo_controller = ModeloController()
    app.register_blueprint(entrega_controller.bp)
    app.register_blueprint(diretoria_controller.bp)
    app.register_blueprint(avaliacoes_controller.bp)
    # app.register_blueprint(modelo_controller.bp)

    app.register_blueprint(fornecedor_controller.bp)
    app.register_blueprint(transportadora_controller.bp)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

application = create_app()

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=4000, debug=True)
