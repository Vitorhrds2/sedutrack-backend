import pandas as pd
import joblib
import numpy as np
from flask import jsonify
import pickle
import os
from joblib import load, dump


class ModeloService:
    def __init__(self, 
                 model,
                 matrix = 'app/modelo/df_escola_fornecedor_mean.pkl',
                 normalized_matrix = 'app/modelo/df_normalizado_escola_fornecedor_mean.pkl'):
        
        current_directory = os.path.dirname(os.path.realpath(__file__))
        print(current_directory)

        self.matrix = pd.read_pickle(matrix)
        self.normalized_matrix = pd.read_pickle(normalized_matrix)
        model = load(model)
        self.model = model
    def get_model_prediction(self, modelo_data):

        # Obtém indices dos vizinhos próximos (KNN)
        distances, indices = self.model.kneighbors(self.normalized_matrix)

        # Obtém índice da escola a partir do nome
        school_index = np.where(self.matrix.index==modelo_data['school_name'])[0][0]

        # Seleciona os índices das Escolas mais próximas para a Escola alvo.
        neighbor_indices = indices[school_index, 1:]  

        # Obtém as classificações que essas Escolas próximas deram para o Fernecedor especificado
        neighbor_ratings = self.matrix.loc[:, modelo_data['supplier_name']].iloc[neighbor_indices]

        # Calcular a média das classificações dos vizinhos
        predicted_rating = neighbor_ratings.mean()

        dict = {'predicted_rating': predicted_rating}
        return dict

    