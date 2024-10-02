import pandas as pd
import joblib
import warnings

def process(data):
    # Преобразуем словарь в DataFrame
    data_df = pd.DataFrame([data])

    # Загружаем обученную модель
    loaded_LR = joblib.load('RF_model.joblib')

    # Предсказываем стоимость
    price = loaded_LR.predict(data_df).astype(int)

    # Убираем квадратные скобки и переводим стоимость в миллионы
    price = price[0]  # результат будет одномерным массивом
    price = round(price / 1_000_000, 3)

    return price
