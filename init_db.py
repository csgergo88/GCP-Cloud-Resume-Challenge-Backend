from google.cloud import firestore

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
db = firestore.Client(project="resumechallangetest")
data = {"counter": "0"}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection("visitorcounter").document("VC").set(data)