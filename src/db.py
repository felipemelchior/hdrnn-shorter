import redis
from redis.exceptions import ConnectionError

def connect_redis(): 
    redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

    try:
        redis_client.ping()
        print("Connected to Redis!")
        return redis_client
    except redis.ConnectionError:
        print("Unable to connect to Redis.")