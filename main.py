from flask import Flask, request, jsonify, render_template
import base64

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/upload-drawing', methods=['POST'])
def upload_drawing():
    global counter
    counter = counter + 1
    data = request.json['image']
    image_data = data.split(",")[1]
    with open("drawing.png", "wb") as fh:
        fh.write(base64.b64decode(image_data))
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)