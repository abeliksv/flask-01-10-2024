from flask import Flask, render_template, request
from processingS import process

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

    if request.method == "POST":
        # Получаем значения, введённые пользователем
        total_area = request.form.get("total_area", 35)
        floor = request.form.get("floor", 5)
        min_to_metro = request.form.get("min_to_metro", 10)
        construction_year = request.form.get("construction_year", 2005)
        number_of_rooms = request.form.get("number_of_rooms", 1)
        ceiling_height = request.form.get("ceiling_height", 2.7)

        # Собираем данные в словарь
        data = {
            'min_to_metro': int(min_to_metro),
            'total_area': float(total_area),
            'floor': float(floor),
            'construction_year': int(construction_year),
            'ceiling_height': float(ceiling_height),
            'number_of_rooms': int(number_of_rooms)
        }

        # Обрабатываем данные и считаем цену
        price = process(data)

        # Сообщение с результатом расчета
        message = f"Стоимость недвижимости {price} млн. руб."

    # Передаем все переменные в шаблон для отображения
    return render_template("index.html",
                           total_area=total_area,
                           floor=floor,
                           min_to_metro=min_to_metro,
                           construction_year=construction_year,
                           number_of_rooms=number_of_rooms,
                           ceiling_height=ceiling_height,
                           message=message)


if __name__ == "__main__":
    app.run()
