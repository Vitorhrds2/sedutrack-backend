import pandas as pd
import joblib
import numpy as np
from flask import jsonify
import pickle
import os
from joblib import load, dump


class ModeloService:
    def __init__(self, 
                 model = 'app/modelo/knn_model.joblib',
                 matrix = 'app/modelo/df_escola_fornecedor_mean.joblib',
                 normalized_matrix = 'app/modelo/df_normalizado_escola_fornecedor_mean.joblib'):
        
        current_directory = os.path.dirname(os.path.realpath(__file__))
        print(current_directory)

        self.model = load(model)
        self.matrix = load(matrix)
        self.normalized_matrix = load(normalized_matrix)

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

    