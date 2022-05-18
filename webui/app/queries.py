from functools import lru_cache

from . import client


@lru_cache
def get_all_sql_entities():
    return client.sql.get_all()
