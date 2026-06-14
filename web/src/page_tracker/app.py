import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    try:  # pylint: disable=R1705
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{THIKNING FACE}", 500
    else:
        return f"This page has been seen {page_views} times."


@cache
def redis():
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


if __name__ == "__main__":
    app.run()
