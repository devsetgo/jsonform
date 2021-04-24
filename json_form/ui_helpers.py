# -*- coding: utf-8 -*-
from pydantic import  Field
from pydantic.fields import Undefined, FieldInfo
from typing import Any

class NumberTypes:
    range: dict = {"ui:widget": "range"}
    updown: dict = {"ui:widget": "updown"}
    radio: dict = {"ui:widget": "radio"}


class BoolTypes:
    checkbox: dict = {"ui:widget": "checkbox"}
    select: dict = {"ui:widget": "select"}
    radio: dict = {"ui:widget": "radio"}


class StringTypes:
    text_box: dict = {"ui:widget": "text"}
    password: dict = {"ui:widget": "password"}
    color: dict = {"ui:widget": "color"}
    text_area: dict = {"ui:widget": "textarea"}
    email: dict = {"ui:widget": "email"}
    uri: dict = {"ui:widget": "uri"}
    data_url: dict = {"ui:widget": "data-url"}
    date: dict = {"ui:widget": "date"}
    date_time: dict = {"ui:widget": "date-time"}


class HiddenTypes:
    hidden = {"ui:widget": "hidden"}


class ElementTypes:
    Hiden = {"ui:widget": "hidden"}



def BoolField(    
    default: Any = Undefined,
    alias: str = None,
    title: str = None,
    description: str = None,
    const: bool = None,            
) -> Any:
    
    extra = {}
    extra['ui_widget']= BoolTypes.radio

    field_info = FieldInfo(
        default,
        default_factory=None,
        alias=alias,
        title=title,
        description=description,
        const=const,
        gt=None,
        ge=None,
        lt=None,
        le=None,
        multiple_of=None,
        min_items=None,
        max_items=None,
        min_length=None,
        max_length=None,
        allow_mutation=True,
        regex=None,
        extra=extra,
    )
    field_info._validate()
    return field_info


def CheckboxField(    
    default: Any = Undefined,
    alias: str = None,
    title: str = None,
    description: str = None,
    const: bool = None,            
) -> Any:
    
    extra = {}
    extra['ui_widget']= BoolTypes.checkbox

    field_info = FieldInfo(
        default,
        default_factory=None,
        alias=alias,
        title=title,
        description=description,
        const=const,
        gt=None,
        ge=None,
        lt=None,
        le=None,
        multiple_of=None,
        min_items=None,
        max_items=None,
        min_length=None,
        max_length=None,
        allow_mutation=True,
        regex=None,
        extra=extra,
    )
    field_info._validate()
    return field_info

def BoolSelectBoxField(    
    default: Any = Undefined,
    alias: str = None,
    title: str = None,
    description: str = None,
    const: bool = None,            
) -> Any:
    
    extra = {}
    extra['ui_widget']= BoolTypes.select

    field_info = FieldInfo(
        default,
        default_factory=None,
        alias=alias,
        title=title,
        description=description,
        const=const,
        gt=None,
        ge=None,
        lt=None,
        le=None,
        multiple_of=None,
        min_items=None,
        max_items=None,
        min_length=None,
        max_length=None,
        allow_mutation=True,
        regex=None,
        extra=extra,
    )
    field_info._validate()
    return field_info

