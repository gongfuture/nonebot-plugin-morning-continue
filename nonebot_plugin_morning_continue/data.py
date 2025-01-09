from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum

class MessageType(str, Enum):
    morning = "morning"
    evening = "evening"

class MessageData(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int = Field(..., gt=0)
    timestamp: int = Field(..., gt=0)
    messageid: int = Field(..., gt=0)
    userid: int = Field(..., gt=0)
    messagetype: MessageType
    groupid: int

    @field_validator('groupid')
    @classmethod
    def validate_groupid(cls, v):
        if v > 0 or v == -1:
            return v
        raise ValueError('groupid 必须为正数或 -1')