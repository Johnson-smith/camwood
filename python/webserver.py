from flask import Flask
from flask import request 

app = Flask(__name__)  # type: Flask

@app.route("/test")
def index():
    ip=request.headers['X-Real-IP']
    return ip



if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000, host='0.0.0.0')