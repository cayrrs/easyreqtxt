import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint


def plot_dataframe(df):
    fig, ax = plt.subplots()
    ax.plot(df["x"], df["y"])
    return fig


def summarize(df):
    pprint(df.describe())
    return np.mean(df["y"])
