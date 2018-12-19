from flask import Flask
from flask import request 

app = Flask(__name__)  # type: Flask

@app.route("/")
def index():
    return '路由到客户机228'



if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000, host='0.0.0.0')