from flask import Flask, render_template, request

from processing import process

app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def index():
    message = ''
    if request.method == "POST":
        total_area = request.form.get("total_area")
        floor = request.form.get("floor")
        cost = process(float(total_area),float(floor))
        message = f"Стоимость недвижимости {cost}"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
