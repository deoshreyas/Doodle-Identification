from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import base64

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/drawing.png')
def serve_drawing():
    return send_from_directory('.', 'drawing.png')

@app.route('/upload-drawing', methods=['POST'])
def upload_drawing():
    data = request.json['image']
    image_data = data.split(",")[1]
    with open("drawing.png", "wb") as fh:
        fh.write(base64.b64decode(image_data))
    # Emit a message to the frontend
    socketio.emit('image_saved', {'status': 'success'})
    return jsonify({'status': 'success'})  # Acknowledge the image was processed

if __name__ == '__main__':
    socketio.run(app, debug=True)