# load traning and testing data
# scale the traning data
# save the scaler data into processed folder
from sklearn.preprocessing import StandardScaler
from data_preprocessing import load_and_split_data
import pandas as pd
import pickle


x_train, x_test, y_train, y_test=load_and_split_data()

scaler = StandardScaler()
x_train_scaled= scaler.fit_transform(x_train)

x_test_scaled=scaler.transform(x_test)

# save the scaler data into processed folder
pd.DataFrame(x_train_scaled).to_csv("../data/processed/x_train.csv",index=False)
pd.DataFrame(x_test_scaled).to_csv("../data/processed/x_test.csv",index=False)
pd.DataFrame(y_train).to_csv("../data/processed/y_train.csv",index=False)
pd.DataFrame(y_test).to_csv("../data/processed/y_test.csv",index=False)

with open("../artifacts/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)