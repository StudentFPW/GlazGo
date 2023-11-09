import redis
import os

from dotenv import load_dotenv

load_dotenv()

red = redis.Redis(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    password=os.getenv("PASSWORD"),
)

# red.flushall()
