from pydantic import BaseModel, field_validator
from nonebot import logger


class ScopedConfig(BaseModel):
    plugin_enabled: bool = True
    command_need_at: bool = False
    command_priority: int = 15

    @field_validator('command_priority')
    @classmethod
    def check_command_priority(cls, v: int) -> int:
        if v >= 1:
            return v
        logger.error('command_priority must be greater than or equal to 1')
        raise ValueError('command_priority must be greater than or equal to 1')


class Config(BaseModel):
    morning_cont: ScopedConfig
