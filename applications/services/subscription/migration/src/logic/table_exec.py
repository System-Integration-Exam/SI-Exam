from connection.sqlite_connection import execute_query
from utils.query_utils import get_all_up_scripts, get_all_down_scripts


def migrate_down() -> None:
    print("migrate down...")
    for script in get_all_down_scripts():
        execute_query(script)


def migrate_up() -> None:
    print("migrate up...")
    for _ in range(2):
        for script in get_all_up_scripts():
            execute_query(script)
