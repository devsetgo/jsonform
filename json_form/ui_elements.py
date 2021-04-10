# -*- coding: utf-8 -*-


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
    Hiden={"ui:widget": "hidden"}