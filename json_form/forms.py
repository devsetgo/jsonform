# -*- coding: utf-8 -*-
import csv
import json
import os
import random
from datetime import datetime
from pathlib import Path
from typing import List
import logging

from json_form import form_templates
from jinja2 import Template

from pydantic.schema import schema

log_format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

# logging.basicConfig(format=log_format, level=logging.DEBUG)

# form = VerticalLayout(
#         HorizontalLayout(
#             Text("firstname"),
#             Text("lastname"),        
#             City(),
#             State(),
#             Zip()
#         ),
#         HorizontalLayout(
#             Phone(),
#             Email(),            
#         )
# )



def form_engine(
    schema_model: dict,
    endpoint: str = None,
    # ui_schema: dict = None,
    form_data: dict = None,
    template_type: str = None,
):

    template_used = form_templates.FULL_PAGE_TWO

    if template_type is None:

        template_type: str = "FULL_PAGE"
        template_used = form_templates.FULL_PAGE_TWO

    # logging.debug(schema_model)
    form_model = schema_model.schema()
    # print(schema_dict)
    # schema = schema_generator(data_schema=form_model)
    ui_schema = uiSchema_generator(data_schema=form_model)

    pydantic_schema_form: dict = {"schema": form_model, "uiSchema": ui_schema}
    print(pydantic_schema_form)
    template = Template(template_used)
    logging.info(f"Template used {template_type}")
    result = template.render(pydantic_schema_form=pydantic_schema_form)
    return result


def ui_widget_fields(d):
    for k,v in d['properties'].items():
        widget_name = k
        if 'extra' in v:            
            if 'ui_widget'in v['extra']:                
                yield widget_name, v['extra']['ui_widget']
                
def generate_ui_schema(d):
    fields = {k:v for k, v in ui_widget_fields(d)}
    return fields


def uiSchema_generator(data_schema):
    print("data_schema:")
    # print(data_schema)
    data = data_schema.copy()
    # return data["uiSchema"]
    schema= generate_ui_schema(data)
    print(schema)
    return schema


def schema_generator(data_schema):
    data = data_schema.copy()
    data.pop("uiSchema")
    return data
