from flask import Flask, render_template, request
from processingS import process, preprocess
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    # Значения по умолчанию
    total_area = 35
    floor = 5
    min_to_metro = 10
    construction_year = 2005
    number_of_rooms = 1
    ceiling_height = 2.7
    message = ''
    errors = []

    if request.method == "POST":
        # Очищаем сообщение перед новым расчетом
        message = ''

        # Получаем значения, введённые пользователем и преобразуем их в числа
        try:
            total_area = float(request.form.get("total_area", 35))
            floor = int(request.form.get("floor", 5))
            min_to_metro = int(request.form.get("min_to_metro", 10))
            construction_year = int(request.form.get("construction_year", 2005))
            number_of_rooms = int(request.form.get("number_of_rooms", 1))
            ceiling_height = float(request.form.get("ceiling_height", 2.7))

            # Проверяем, что значения корректны
            if total_area < 9 or total_area > 320:
                errors.append("Площадь должна быть положительным числом от 9 до 320 м.кв.")
            if floor <= 0 or floor > 85:
                errors.append("Этаж должен быть положительным числом, не более 85.")
            if min_to_metro < 0 or min_to_metro > 30:
                errors.append("Время до метро должно быть числом не меньше 0 и не более 30 минут.")
            if construction_year < 1800 or construction_year > 2030:
                errors.append("Год постройки должен быть между 1800 и 2030 годом.")
            if number_of_rooms <= 0 or number_of_rooms > 3:
                errors.append("Количество комнат должно быть положительным числом, не более 3 (ограничение модели).")
            if ceiling_height < 2.3 or ceiling_height > 6:
                errors.append("Высота потолков должна быть в интервале от 2.30 до 6.0")

            if errors:
                message = "<br>".join(errors)
            else:
                # Создание DataFrame
                data = pd.DataFrame({
                    'min_to_metro': [min_to_metro],
                    'total_area': [total_area],
                    'floor': [floor],
                    'construction_year': [construction_year],
                    'ceiling_height': [ceiling_height],
                    'number_of_rooms': [number_of_rooms]
                })

                # Обрабатываем данные
                scaled_data = preprocess(data)

                # Считаем цену
                price = process(scaled_data)
                price = round(price / 1000000, 3)

                # Сообщение с результатом расчета
                message = f"Стоимость недвижимости: {price} млн. рублей"

        except ValueError:
            message = "Пожалуйста, введите корректные числовые значения."

    # Передаем все переменные в шаблон для отображения
    return render_template("index.html",
                           total_area=total_area,
                           floor=floor,
                           min_to_metro=min_to_metro,
                           construction_year=construction_year,
                           number_of_rooms=number_of_rooms,
                           ceiling_height=ceiling_height,
                           message=message,
                           error_messages=errors)


if __name__ == '__main__':
    app.run()
