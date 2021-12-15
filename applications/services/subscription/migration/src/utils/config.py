import os
import toml

# This file is a utility for conversion of the toml file.
# Keep it minimal
# Use config.toml instead.

_ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_ROOT_DIR)
ROOT_DIR: str = os.path.dirname(_ROOT_DIR)
_CONFIG_FILE_PATH: str = ROOT_DIR + "/config.toml"
_filename = _CONFIG_FILE_PATH
_content: str = ""

with open(_filename) as f:
    _content = f.read()


with open(_filename) as f:
    _content = f.read()

CONFIG = toml.loads(_content)
if os.getenv("CONTAINERIZED", None):
    DATABASE_CONFIG = CONFIG["containerized"]["database"]
else:
    DATABASE_CONFIG = CONFIG["development"]["database"]
