import pandas as pd
import numpy as np
import joblib

# from sklearn import metrics
# from sklearn import preprocessing
# from sklearn.linear_model import LinearRegression #линейная регрессия



def process(total_area, floor, min_to_metro, construction_year, number_of_rooms,ceiling_height):

    # price = min_to_metro * floor * total_area * construction_year * number_of_rooms * ceiling_height
    x = np.array([min_to_metro,total_area,floor,construction_year,ceiling_height,number_of_rooms])
    x = x.reshape(1, -1)

    # df_x = np.array([min_to_metro,total_area,floor,construction_year,ceiling_height,number_of_rooms]).reshape(-1,1)

    # Load the saved model from a file
    loaded_LR = joblib.load('LR_model.joblib')

    price  = loaded_LR.predict(x).astype(int)
    price  = price[0,0] #убираем квадратные скобки из выводимого сообщения

    return price
