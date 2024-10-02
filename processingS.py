import pandas as pd
import numpy as np

import joblib

from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression #линейная регрессия



def process(total_area, floor, min_to_metro, construction_year, number_of_rooms,ceiling_height):

    # price = min_to_metro * floor * total_area * construction_year * number_of_rooms * ceiling_height

    df_x = np.array([min_to_metro,total_area,floor,construction_year,ceiling_height,number_of_rooms]).reshape(-1,1)

    with open('LR_model.pkl', 'rb') as f:
        LR = pickle.load(f)

    price = df_x

    return price
