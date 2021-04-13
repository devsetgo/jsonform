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
    schema = schema_generator(data_schema=form_model)
    ui_schema = uiSchema_generator(data_schema=form_model)

    pydantic_schema_form: dict = {"schema": schema, "uiSchema": ui_schema}

    template = Template(template_used)
    logging.info(f"Template used {template_type}")
    result = template.render(pydantic_schema_form=pydantic_schema_form)
    return result


def uiSchema_generator(data_schema):
    data = data_schema.copy()
    return data["uiSchema"]


def schema_generator(data_schema):
    data = data_schema.copy()
    data.pop("uiSchema")
    return data
