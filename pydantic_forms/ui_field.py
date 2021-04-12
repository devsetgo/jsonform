# -*- coding: utf-8 -*-
"""
should have a description
"""
from pydantic import *
from pydantic import BaseModel, Field


class UIField(Field):
    def __init__(self, ui_widget, ui_options=None, *args, **kwargs):
        ui_element = self.ui_widget
        ui_options = self.ui_options

    def ui_element(self):
        pass

    def ui_options(self):
        pass
