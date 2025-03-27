import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

def initialize_firebase():
    if not firebase_admin._apps:
        service_account_key = {
            "type": os.getenv("FIREBASE_TYPE"),
            "project_id": os.getenv("FIREBASE_PROJECT_ID"),
            "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace(r'\n', '\n'),
            "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.getenv("FIREBASE_CLIENT_ID"),
            "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
            "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
            "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
        }
        cred = credentials.Certificate(service_account_key)
        firebase_admin.initialize_app(cred)

def save_perform(data):
    print("1")
    print(os.getenv("FIREBASE_TYPE"))
    print(os.getenv("FIREBASE_PRIVATE_KEY"))
    initialize_firebase()
    print("2")
    db = firestore.client()
    print("3")
    doc_ref = db.collection('exercise').document()
    doc_ref.set(data)
    return doc_ref.id

def save_personalization(exercise_id, data):
    initialize_firebase()
    db = firestore.client()
    exercise_ref = db.collection('exercise').document(exercise_id)
    doc_ref = exercise_ref.collection('personalization').document()
    doc_ref.set(data)
    return doc_ref.id

def get_personalization(exercise_id, personalization_id=None):
    initialize_firebase()
    db = firestore.client()
    exercise_ref = db.collection('exercise').document(exercise_id)
    personalization_collection = exercise_ref.collection('personalization')
    
    if personalization_id:
        # Get specific personalization document
        doc = personalization_collection.document(personalization_id).get()
        return doc.to_dict() if doc.exists else None
    else:
        # Get all personalization documents
        docs = personalization_collection.get()
        return docs[0].to_dict()

# def save_evaluation(data):
#     initialize_firebase()
#     db = firestore.client()
    
#     # Check for existing document with matching exerciseId
#     existing_docs = db.collection('evaluation')\
#                      .where('exerciseId', '==', data['exerciseId'])\
#                      .get()
    
#     if existing_docs:
#         # Update existing document with new data in type-specific field
#         existing_doc = existing_docs[0].reference
#         update_data = {data['type']: data}
#         existing_doc.set(update_data, merge=True)
#         return existing_doc.id
#     else:
#         # Create new document if no existing match
#         doc_ref = db.collection('evaluation').document()
#         doc_ref.set(data)
#         return doc_ref.id

def save_evaluation(exercise_id, type, data):
    initialize_firebase()
    db = firestore.client()
    exercise_ref = db.collection('exercise').document(exercise_id)
    doc_ref = exercise_ref.collection('evaluation').document(type)
    doc_ref.set(data)
    return doc_ref.id

def save_feedback(exercise_id, data):
    initialize_firebase()
    db = firestore.client()
    exercise_ref = db.collection('exercise').document(exercise_id)
    doc_ref = exercise_ref.collection('feedback').document()
    doc_ref.set(data)
    return doc_ref.id

def get_feedback(exercise_id, type=None):
    initialize_firebase()
    db = firestore.client()
    exercise_ref = db.collection('exercise').document(exercise_id)
    feedback_collection = exercise_ref.collection('feedback')
    docs = feedback_collection.where('type', '==', type).get()

    return [doc.to_dict() for doc in docs]
    
def get_analysis(exercise_id):
    initialize_firebase()
    db = firestore.client()
    exercise_ref = db.collection('exercise').document(exercise_id)
    doc = exercise_ref.get()
    return doc.to_dict()