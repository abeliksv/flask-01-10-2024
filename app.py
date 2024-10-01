from flask import Flask, render_template, request

from processing import process

app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def index():
    message = ''
    if request.method == "POST":
        total_area = request.form.get("total_area")
        floor = request.form.get("floor")
        min_to_metro = request.form.get("min_to_metro")
        construction_year = request.form.get("construction_year")
        number_of_rooms = request.form.get("number_of_rooms")
        price = process(float(total_area),float(floor),int(min_to_metro),int(construction_year),int(number_of_rooms))
        message = f"Стоимость недвижимости {price}"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
