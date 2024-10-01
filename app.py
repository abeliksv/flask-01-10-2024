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
        price = process(float(total_area),float(floor),float(min_to_metro))
        message = f"Стоимость недвижимости {price}"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
