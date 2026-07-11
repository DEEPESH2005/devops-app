from flask import Flask, jsonify, render_template
import socket
import time
import math
import os

app = Flask(__name__)

start_time = time.time()
visit_count = 0


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    """Health check endpoint - used later by monitoring / load balancer / load testing"""
    return jsonify({
        "status": "ok",
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - start_time, 2)
    }), 200


@app.route('/api/info')
def info():
    """Simple API endpoint"""
    global visit_count
    visit_count += 1
    return jsonify({
        "message": "Hello from your DevOps assignment app (Python/Flask)!",
        "hostname": socket.gethostname(),
        "platform": os.name,
        "visit_count": visit_count
    })


@app.route('/api/compute')
def compute():
    """Slightly heavier endpoint on purpose - useful for load testing (CPU work)"""
    n = 1000000
    total = 0.0
    for i in range(n):
        total += math.sqrt(i)
    return jsonify({"result": total, "iterations": n})


if __name__ == '__main__':
    # 0.0.0.0 so it's reachable from outside the container/EC2 instance
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))