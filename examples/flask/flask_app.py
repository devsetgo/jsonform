from json_form.forms import form_engine


from flask import Flask
from flask import request

app = Flask(__name__)


from enum import Enum
from pydantic import BaseModel, Field


class FooBar(BaseModel):
    count: int
    size: float = None


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    foo_bar: FooBar = Field(...)
    gender: Gender = Field(None, alias="Gender")
    snap: int = Field(
        42,
        title="The Snap",
        description="this is the value of snap",
        gt=30,
        lt=50,
    )

    class Config:
        title = "Main"


@app.route("/", methods=["GET", "POST"])
def index():
    result = form_engine(pydantic_model=MainModel)

    if request.method == "POST":
        print(request.form)

    return result


if __name__ == "__main__":
    app.run()
