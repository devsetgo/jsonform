from enum import Enum
import pydantic


class FooBar(pydantic.BaseModel):
    count: int
    size: float = None


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class MainModel(pydantic.BaseModel):
    """
    This is the description of the main model
    """

    foo_bar: FooBar = pydantic.Field(...)
    gender: Gender = pydantic.Field(None, alias="Gender")
    snap: int = pydantic.Field(
        42,
        title="The Snap",
        description="this is the value of snap",
        gt=30,
        lt=50,
    )

    class Config:
        title = "Main"
