from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify(message="Merhaba, Docker ile çalışan API!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
