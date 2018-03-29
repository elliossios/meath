from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def get_location():
    lat = 55.21123
    lon = 12.412
    return jsonify(lat=lat, long=lon)
    
if __name__ == "__main__":
    app.run(host= '0.0.0.0')