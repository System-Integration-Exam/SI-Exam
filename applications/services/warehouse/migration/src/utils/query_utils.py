import os
import os.path
from utils.config import CONFIG, ROOT_DIR


FULL_MIGRATION_DIRECTORY = (
    f"{ROOT_DIR}/{CONFIG['misc']['migration_directory']}")


def _get_sql(path: str) -> str:
    return open(f"{path}").read()


def _try_parse(value):
    try:
        return int(value)
    except ValueError:
        return None
    
    
    
def _get_all_migrations():
    return [entry.name for entry in os.scandir(
        _get_newest_version_path()) if entry.is_dir()]


def get_all_up_scripts() -> list:
    return [_get_sql(f"{_get_newest_version_path()}/{path}/up.sql") for path in _get_all_migrations()]


def get_all_down_scripts() -> list:
    return [_get_sql(f"{_get_newest_version_path()}/{path}/down.sql") for path in _get_all_migrations()]