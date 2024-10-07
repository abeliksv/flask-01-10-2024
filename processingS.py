import pandas as pd
import numpy as np
import joblib



def process(data):
    # Преобразуем словарь в DataFrame
    data_df = pd.DataFrame([data])

    # Загружаем обученную модель
    # loaded_model = joblib.load('RF_model.joblib')
    loaded_model = joblib.load('LR_model.joblib')

    # Предсказываем стоимость
    price = loaded_model.predict(data_df).astype(int)

    # Убираем квадратные скобки и переводим стоимость в миллионы
    price = price[0,0]  # результат будет одномерным массивом
    # price = round(price / 1_000_000, 3)# применять при загрузке RF_model.joblib
    price = np.round(price / 1_000_000, 3)


    return price
