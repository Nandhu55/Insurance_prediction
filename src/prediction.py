# 1.load scaler file and model.pkl files
# 2.create a function to predict

import pickle
import numpy as np

class Insurance_Prediction:
    def __init__(self):
        with open("artifacts/scaler.pkl","rb") as f:
            self.scaler=pickle.load(f)
        with open("artifacts/model.pkl","rb") as f:
            self.model=pickle.load(f)
    def prediction(self,Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs):
        input_array = np.array([[Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs]]).reshape(1, -1)
        input_scaled = self.scaler.transform(input_array)
        result = self.model.predict(input_scaled)
        return result[0][0]