from connection.sqlite_connection import execute_query
from utils.query_utils import get_all_up_scripts, get_all_down_scripts



def migrate_down() -> None:
    for script in get_all_down_scripts():
        execute_query(script)


def migrate_up() -> None:
    for _ in range(3):
        for script in get_all_up_scripts():
            execute_query(script)
