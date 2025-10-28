from flask import Flask, request
import json, time, redis, os

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis-server")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

TTL_SECONDS = 600  # 10 minutes

def get_cached(key):
    data = r.get(key)
    if data is None:
        return None
    data = json.loads(data)
    if time.time() - data["time"] <= TTL_SECONDS:
        return data["html"]
    return None

def set_cached(key, html):
    r.set(key, json.dumps({"html": html, "time": time.time()}))

@app.route("/")
def index():
    key = "index"
    cached = get_cached(key)
    if cached:
        return cached
    html = f"<h1>Hello from Flask</h1><p>Time: {time.ctime()}</p>"
    set_cached(key, html)
    return html

@app.route("/about")
def about():
    key = "about"
    cached = get_cached(key)
    if cached:
        return cached
    html = "<h1>About</h1><p>This page is cached for 10 minutes.</p>"
    set_cached(key, html)
    return html

if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 5000)
