from pathlib import Path
from nonebot import require
import functools

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store

cache_dir: Path = store.get_plugin_cache_dir()
config_dir: Path = store.get_plugin_config_dir()
data_dir: Path = store.get_plugin_data_dir()

