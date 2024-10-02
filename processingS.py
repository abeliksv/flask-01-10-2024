import numpy as np
import joblib

def process(total_area, floor, min_to_metro, construction_year, number_of_rooms,ceiling_height):

    # формируем вектор для predict
    x = np.array([min_to_metro,total_area,floor,construction_year,ceiling_height,number_of_rooms]).reshape(1, -1)

    # Load the saved model from a file LR_model.joblib
    loaded_LR = joblib.load('LR_model.joblib')

    price  = loaded_LR.predict(x).astype(int)
    price  = price[0,0] #убираем квадратные скобки из выводимого сообщения
    price = round(price/1000000, 3) # переводим стоимость в млн. и округляем до 3-х знаков

    return price
