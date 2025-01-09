from nonebot import require, on_command, logger, get_plugin_config
from nonebot.adapters.onebot.v11 import 
require("nonebot_plugin_saa")



morning = on_command("morning", aliases={"早安", "早上好", "早"}, priority=5, block=True)
