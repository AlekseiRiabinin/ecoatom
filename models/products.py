from pydantic import BaseModel, Field


class X(BaseModel):
    key: str = Field()
    val: int = Field(gt=0)


class Source(BaseModel):
    name: str = Field()
    plastic: int = Field(default=0)
    glass: int = Field(default=0)
    biowaste: int = Field(default=0)


class Storage(BaseModel):
    name: str = Field()
    max_plastic: int = Field()
    max_glass: int = Field()
    max_biowaste: int = Field()
    plastic: int = Field(default=0)
    glass: int = Field(default=0)
    biowaste: int = Field(default=0)
