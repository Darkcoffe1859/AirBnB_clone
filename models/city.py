#1/usr/bin/python3
"""
Module City class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        state_id: (str) will be state.id
        name:     (str)
    """
    state_id = ""
    name = ""

