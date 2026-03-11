# load raw data
# identifying x and y (in or out)
# split data into train and test

import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data():
    data= pd.read_csv("../data/raw/insurance.csv")
    x= data[[  "Age","Annual_Income_LPA", "Policy_Term_Years", "Sum_Assured_Lakhs"]]
    y= data["Annual_Premium_Thousands"]
    x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test