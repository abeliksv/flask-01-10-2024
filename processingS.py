import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression #линейная регрессия



def process(total_area, floor, min_to_metro, construction_year, number_of_rooms,ceiling_height):
    # TODO: Интегрировать модель машинного обучения
    # price = min_to_metro * floor * total_area * construction_year * number_of_rooms * ceiling_height

    df_x = [min_to_metro, total_area, floor, construction_year,ceiling_height,number_of_rooms]
    price = df_x

    #min_max_scaler_x = preprocessing.MinMaxScaler()
    # min_max_scaler_y = preprocessing.MinMaxScaler()
    #
    # scaled_x = min_max_scaler_x.fit_transform(df_x)
    # scaled_y = min_max_scaler_y.fit_transform(df_y)

    return price
