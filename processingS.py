import pandas as pd
import joblib


def preprocess(data):
    try:
        min_max_scaler_x = joblib.load('./models/min_max_scaler_x.joblib')
        print("Scaler_x loaded successfully.")
    except FileNotFoundError:
        print("Error: Joblib file min_max_scaler_x.joblib not found.")
        return None
    except Exception as e:
        print(f"An error_x occurred: {e}")
        return None
    scaled_data = min_max_scaler_x.transform(data)
    return scaled_data


def process(scaled_data):
    try:
        min_max_scaler_y = joblib.load('./models/min_max_scaler_y.joblib')
        print("Scaler_y loaded successfully.")
    except FileNotFoundError:
        print("Error: Joblib file min_max_scaler_y.joblib not found.")
        return None
    except Exception as e:
        print(f"An error_y occurred: {e}")
        return None
    # Преобразуем в DataFrame
    data_df = pd.DataFrame(scaled_data)
    # Загружаем обученную модель
    loaded_model = joblib.load('models/LR_model_scaled.joblib')
    # Предсказываем стоимость
    scaled_price = loaded_model.predict(data_df)
    price = min_max_scaler_y.inverse_transform([scaled_price]).squeeze()
    # Убираем квадратные скобки squeeze()
    return price