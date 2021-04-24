from enum import Enum
import json
from typing import List, Dict
from pydantic import BaseModel, Field
from pydantic.schema import schema, field_schema
from json_form.ui_helpers import BoolTypes, HiddenTypes, StringTypes, NumberTypes


class FooBar(BaseModel):
    count: int
    size: float = Field(
        42.0,
        title="The Size",
        description="this is the value of size",
        gt=30,
        lt=50,
    )


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


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
    foo_bar: FooBar = Field(...)
    gender: Gender = Field(..., alias="Gender")
    snap: int = Field(
        42,
        title="The Snap",
        description="this is the value of snap",
        gt=30,
        lt=50,
        ui_type=NumberTypes.range,
    )

    class Config:
        title = "Example Form"
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


class BoolModels(BaseModel):
    """
    This is an example of building a model for bool types
    """

    this_is_checkbox: bool = Field(..., title="check box type")
    this_is_select: bool = Field(..., title="select type")
    this_is_radio: bool = Field(..., title="radio type")


class GenderSelect(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class StringExample(BaseModel):
    """
    This is an example of building a model for string types
    """

    text_box_object: str = Field(
        ..., title="text box example", min_length=4, max_length=100
    )
    password: str = Field(..., title="password type", min_length=4, max_length=30)
    color: str = Field(..., title="color type")
    text_area: str = Field(..., title="text area type", min_length=4, max_length=1000)
    email: str = Field(..., title="email type", min_length=4, max_length=100)
    uri: str = Field(..., title="url type", min_length=4)
    data_url: str = Field(..., title="data url type")
    date: str = Field(..., title="date type")
    date_time: str = Field(
        ..., title="date time type", ui_element=StringTypes.date_time
    )
    gender: GenderSelect = Field(...)


class BooksModels(BaseModel):
    name: str = Field(..., title="book name", min_length=2, max_length=40)
    isbn: str


class ExampleModel(BaseModel):
    """
    This is an example of building a model
    """

    books: List[BoolModels] = None
    bool_example: BoolModels
    string_example: StringExample
    first_name: str = Field(
        None,
        title="First Name",
        description="your first name",
        ui_widget=HiddenTypes.hidden,
        ui_options="pdf",
    )
    last_name: str = Field(None, title="Last Name")
    password: str

    class Config:
        title = "Francis"
        # schema_extra = {
        #     "uiSchema": {
        #         "bool_example": {
        #             "this_is_checkbox": {"ui:widget": "checkbox","ui:options": { 'accept': ".pdf" }},
        #             "this_is_select": BoolTypes.checkbox,
        #             "this_is_radio": BoolTypes.radio,
        #         },
        #         "string_example": {
        #             "text_box": StringTypes.text_box,
        #             "password": StringTypes.password,
        #             "color": StringTypes.color,
        #             "text_area": StringTypes.text_area,
        #             "email": StringTypes.email,
        #             "uri": StringTypes.uri,
        #             "data_url": StringTypes.data_url,
        #             "date": StringTypes.date,
        #             "date_time": StringTypes.date_time,

        #         },
        #     }
        # }
