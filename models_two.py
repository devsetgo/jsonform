from enum import Enum
import json
from typing import List
from pydantic import BaseModel, Field, PrivateAttr
from pydantic.schema import schema, field_schema
from pydantic.utils import generate_model_signature
from json_form.ui_elements import BoolTypes, HiddenTypes, StringTypes, NumberTypes


class NameModel(BaseModel):
    name:str
    number:str

class SimpleModel(BaseModel):
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
    contact:List[NameModel]

    class Config:
        title = "Main"
        schema_extra = {
            "uiSchema": {
                "example": StringTypes.date_time,
                "this_true": BoolTypes.radio,
                "bunch_of_text": StringTypes.text_area,
                "snap": NumberTypes.range,
                "gender": NumberTypes.radio,
                },
            }
        



# print(SimpleModel.schema_json(indent=2))
