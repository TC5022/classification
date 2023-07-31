from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    img_data = request.form['image_data']
    response = jsonify(util.classify_image(img_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python server")
    util.load_saved_artefacts()
    app.run(port=5000)