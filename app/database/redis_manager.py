from multiprocessing.forkserver import connect_to_new_process
from redis import Redis
from redis.exceptions import DataError, ResponseError
from json import dumps, loads
import os

class RedisManager():
    
    def __init__(self, host='cache', port=6379, password='passwordtest', db=0):
        redis_config = {
            "host": os.getenv("REDIS_HOST", host),
            "port": int(os.getenv("REDIS_PORT", port)),
            "password": os.getenv("REDIS_AUTH", password),
            "db": db,
            "decode_responses": False,
            "socket_connect_timeout": 5,
        }
        self.client = Redis(**redis_config)
        
        
    def store(self, word, response):
        self.client.set(word, response)
        
    def get(self, word):
        try:
            response = self.client.get(word)
        except (DataError, ResponseError):
            return None
        
        if not response:
            return None
        
        return response

    def clear(self):
        self.client.flushdb()
        self.client.flushall() 