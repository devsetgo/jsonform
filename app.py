from json_form.forms import form_engine


from flask import Flask
from flask import request
from model import MainModel, ExampleModel

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    result = form_engine(schema_model=ExampleModel)

    if request.method == "POST":
        print(request.form)

    return result


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        print(request.form)
    return dict(request.form)


if __name__ == "__main__":
    app.run()
