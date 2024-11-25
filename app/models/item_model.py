from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class PyObjectId(ObjectId):
    """
    Custom ObjectId class to validate MongoDB ObjectIds in Pydantic models.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError(f"Invalid ObjectId: {value}")
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema):
        """
        Customizes how PyObjectId appears in the JSON Schema.
        """
        schema.update(type="string")
        return schema


class Item(BaseModel):
    """
    Pydantic model for items stored in MongoDB.
    """
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        populate_by_name = True  # Replaces allow_population_by_field_name in Pydantic v2
        arbitrary_types_allowed = True  # Allows non-standard types like ObjectId
        json_encoders = {ObjectId: str}  # Encodes ObjectId as a string in JSON
