from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'''
    <html>
      <head><title>Docker Lab</title></head>
      <body style="font-family: sans-serif; text-align: center; margin-top: 100px;">
        <h1>Hello from Docker Container!</h1>
        <p>This page has been visited <strong>{count}</strong> times.</p>
        <p style="color: #888;">Backend: Flask + Redis</p>
      </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)