from enum import Enum
import json
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field, PrivateAttr
from pydantic.schema import schema, field_schema
from pydantic.types import UUID1
from pydantic.utils import generate_model_signature
from json_form.ui_helpers import BoolTypes, HiddenTypes, StringTypes, NumberTypes
from json_form.ui_helpers import BoolField,CheckboxField,BoolSelectBoxField


class CurrencyType(str, Enum):
    kwd="Kuwaiti Dinar"
    bhd="Bahraini Dinar"
    omr="Omani Rial"
    jod="Jordanian Dinar"
    gbp="British Pound Sterling"
    kyd="Cayman Islands Dollar"
    eur="European Euro"
    chf="Swiss Franc"
    usd="US Dollar"
    cad="Canadian Dollar"
    aud="Australian Dollar"
    sgd="Singapore Dollar"

class NameModel(BaseModel):
    first_name: str = Field(...,title="given name",description="Please enter your first name", min_length=1, max_length=50)
    last_name: str = Field(...,title="surname",description="Please enter your last name",  min_length=1, max_length=50)
    phone_number: str =Field(None,description="123-456-7890", regex="(\d{3}) \D* (\d{3}) \D* (\d{4}) \D* (\d*)")



class SimpleModel(BaseModel):
    """
    This is the description of the main model
    """
    new_radio: bool = BoolField(...,)
    new_checkbox: bool = CheckboxField(...,)
    new_select: bool = BoolSelectBoxField(...,)
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
        gt=10,
        lt=100,
        ui_widget=NumberTypes.range,
    )
    currency:CurrencyType
    email_address:str
    # contact: List[NameModel]

class MyForm(BaseModel):
    
    contact: List[NameModel]
    simple_model:SimpleModel 
    

class RegModel(BaseModel):
    user_id:str
    password:str
    password_two:str


    class Config:
        title = "Example Form"
        # schema_extra = {
        #     "uiSchema": {
        #         "example": StringTypes.date_time,
        #         "this_true": BoolTypes.radio,
        #         "bunch_of_text": StringTypes.text_area,
        #         "snap": NumberTypes.range,
        #         "gender": NumberTypes.radio,
        #         "email_address": StringTypes.email,
        #         "test": BoolTypes.radio,
        #         'new_radio': 'radio',
        #         'new_checkbox': 'checkbox',
        #         'new_select': 'select'
        #     },
        # }


# print(SimpleModel.schema_json(indent=2))
