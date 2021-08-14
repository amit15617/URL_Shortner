import sys
sys.path.append(".")
import redis
from config import logger

REDIS_CONNECTION_POOL = redis.ConnectionPool(
    host="redis",
    port="6379",
    password="am!7ku3ar",
    db=0,
    encoding="utf-8",
    decode_responses=True,
)
redis_client = redis.Redis(connection_pool=REDIS_CONNECTION_POOL)


def get_redis_item(key_):
    """
    Returns redis item
    """
    try:
        response = None
        if redis_client.exists(key_) != 0:
            response = redis_client.get(key_) or None
        if response == "null":
            response = None
    except Exception as ex:
        logger.exception("Critical error in get_redis_item")
        response = None
    logger.debug(f"_get_redis_item {key_} - {response}")
    return response


def set_redis_item(key_, value_):
    """
    Set a redis item
    """
    try:
        redis_client.set(key_, value_)
    except Exception as ex:
        logger.exception("Critical error in set_redis_item")
