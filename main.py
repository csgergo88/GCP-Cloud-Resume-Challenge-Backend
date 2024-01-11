from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import firestore

app = Flask(__name__)
CORS(app)  # Engedélyezzük a CORS-t az alkalmazás számára

# Firestore inicializálása
db = firestore.Client(project='cloudcvchallenge')

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'Bark bark! Ready to roll.'})

@app.route('/<counter>', methods=['GET'])
def get_counter(counter):
    query = db.collection('visitorcount')
    query_snapshot = query.get()
    if len(query_snapshot) > 0:
        return jsonify(query_snapshot[0].to_dict())
    else:
        return jsonify({'status': 'Not found'})

@app.route('/', methods=['POST'])
def update_counter():
    data = request.get_json()
    counter = int(data.get('counter'))

    counter_ref = db.collection('visitorcount').document('334khRyBXlVax4ZFFxuN')
    counter_ref.update({'counter': counter})

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
