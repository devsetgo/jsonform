from enum import Enum
import json
from pydantic import BaseModel, Field, PrivateAttr
from pydantic.schema import schema, field_schema
from pydantic.utils import generate_model_signature
from json_form.ui_elements import BoolTypes, HiddenTypes, StringTypes, NumberTypes


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    this_true: bool = Field(...)
    bunch_of_text: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        title="Big Text Box",
        description="Fill in the text area",
    )
    example: str = Field(...)

    snap: int = Field(
        42,
        title="The Snap",
        description="this is the value of snap",
        gt=30,
        lt=50,
    )

    class Config:
        title = "Main"
        schema_extra = {
            "uiSchema": {
                "example": StringTypes.date_time,
                "this_true": BoolTypes.radio,
                "bunch_of_text": StringTypes.color,
                "snap": NumberTypes.range,
                "gender": NumberTypes.radio,
                "foo_bar": {
                    "size": NumberTypes.updown,
                },
            }
        }


# print(MainModel.schema())
data = MainModel.schema()
x = data.copy()
y = data.copy()
y.pop("uiSchema")
print(x["uiSchema"])
print("----")
print(y)
