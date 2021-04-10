from enum import Enum
import json
from pydantic import BaseModel, Field,PrivateAttr
from pydantic.schema import schema, field_schema
from pydantic.utils import generate_model_signature
from json_form.ui_elements import BoolTypes, HiddenTypes, StringTypes, NumberTypes



class SimpleModel(BaseModel):
    """
    Your description
    """
    first_name:str
    last_name:str
    your_password:str=Field(...,ui_element=StringTypes.text_area)

    class Config:
        title = "Francis"

# print(SimpleModel.schema_json(indent=2))


