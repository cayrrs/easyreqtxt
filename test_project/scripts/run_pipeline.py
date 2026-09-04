from sklearn.linear_model import LinearRegression
import pandas as pd
from dotenv import load_dotenv
import numpy as np
from pathlib import Path

load_dotenv()


def train_model(csv_path):
    df = pd.read_csv(csv_path)
    model = LinearRegression()
    X = np.array(df[["x"]])
    y = np.array(df["y"])
    model.fit(X, y)
    return model
