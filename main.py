from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import firestore
from vars import *

app = Flask(__name__)
CORS(app)  # Enable CORS

# Init Firestore
db = firestore.Client(project)

visitorcount_collection = 'visitorcount'
VC_document = 'VC'

def create_visitorcount_document():
    visitorcount_ref = db.collection(visitorcount_collection).document(VC_document)
    visitorcount_ref.set({'counter': 0})

def get_visitorcount():
    visitorcount_ref = db.collection(visitorcount_collection).document(VC_document)
    document = visitorcount_ref.get()
    if document.exists:
        return document.to_dict()
    else:
        return None

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'Bark bark! Ready to roll.'})

@app.route('/<counter>', methods=['GET'])
def get_counter(counter):
    visitorcount_data = get_visitorcount()
    if visitorcount_data:
        return jsonify(visitorcount_data)
    else:
        create_visitorcount_document()
        return jsonify({'status': 'Not found, creating document. Please refresh'})

@app.route('/', methods=['POST'])
def update_counter():
    data = request.get_json()
    counter = int(data.get('counter'))

    counter_ref = db.collection(visitorcount_collection).document(VC_document)
    counter_ref.update({'counter': counter})

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
