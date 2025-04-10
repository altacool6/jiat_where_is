# proxy_server.py
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/pvd')
def pvd_info():
    try:
        api_url = "http://172.168.15.220:5000/cur_value?topic=v2i-pvd"  # 실제 REST API 주소
        resp = requests.get(api_url)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)