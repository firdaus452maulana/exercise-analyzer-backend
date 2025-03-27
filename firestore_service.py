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
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZzA03hapEA1Pj\ntzUWgggxjx+Cm7gPAyFrbBtl0kYA7KCIIAxvg/xPq1fZtZwwyL/lziVv2nPVdmqI\nFTDVpQf41FZ7zAwiOtCQW9yU9irRWOqyUfEWW9AQVUkoZCpzTFQNsct5hGwG3jmX\nMB6oig0pS23pTWBDTKFmw8Voz23uFeet9AYuyEJZoWQo4SHsIgQ+VoImnT+6t+wU\ntOZlSUIEUNZqlpsufPfYBcnOIZRTUuOs/oj8yy4qURfJ22Cj45r+D9lRmLhkF+vr\nEYmM87OSvyiJJ+BUqV0y4AKDYdRB23jQegjGhTzAwb7fRS9EM2zmEzM/PQ0mJNj4\n4NeWiGxXAgMBAAECggEALJA5VhZ157OsmwfWB3R0u7s2rdEx4HR6BpJYqsVTCIZi\nNGgmUzz0x9Jdx9CGlF7HEPzUoSXYFKHFm3GGi/hYALxls6/k/a3+FcOOBza1PR+N\n6g2lIDeKA4WH0glovC2udxzdbtA/EEqxCvPQGhkhJ0VlSFrKKwsHbVD6V/81VYTq\nCpbpvMxh0e5lSpO5u0uDPVETB7n1Ly9zf6kQwQtZh8G3eb2xF9mwei1r+665gOJ2\nJoCh9AISG8reRKjRZKWmHdmCc36cqb+mL+RcAM/kJuw30v6IAVQvD3lI0jySP7K8\nhE2/FDg9beVDnclO2MfihKd3CX1dRNZYRp/5Tjyn6QKBgQD8U6SYoWUMyPC3a1D/\nwz0LsF040cS00cawUvPrF0BrTc2GR6Jszn2o+9NUXn58sF8z3qtjMv3ZF5rkSF/h\n2OncYJ5ssc151K+QX+/EnBnHRolUUjQZ6Wjw0zwEOo2d47B07nBZBQya7cIFy7oh\n/WUeC5CJhc8IEv2ZB5Z57dhpiQKBgQDc97m6x9nsi8BCHjrM8mnraeofInv0CA7X\nB+ltbaqOgktkJ3mmK3t1sZQYpvCH/BGv/1+iSYUgzgD9Il6jaPPK8DC6md/g8Nxn\nMp2pdzcgLk6Jl/mlQro+qEZp1TnOG2hDrLFV/aPIy7i5N/N3nIeDWlf7Rax4jVVL\ngyGIGocO3wKBgBccxj/g0LO6GCqE3vd+d7IBZpiUxlLVwEBYaNVI3PK3PrMlDqCu\nzV3UK0hYG3fqY94JcGN2wT/IZLyyUG4Mg2dXRkuogay+KZKs5vZ4YfgZ4uxhVzpk\nYeNlReMRRfWHbJtZV9sflkb+rj3/qj4AyulUn9mo8wzHSIli44qpmaAZAoGBAKpK\ntDVxTc6SCVIrT++gpuaJkqf6AIMaLq2jaE8wJDB907JVBdh9TEFw4Ix7I4X5SnxT\nmBVPCa01deeftEXFXZU5tKQqcDJADevuQzlWKgLADUDXActN+JDPSKzJaiogTyNQ\nlL6Loczey/baWuUEmh8t4f5BPOEPMvvmDFKC9zELAoGAEJedFgrOPjKf/kYWrUE6\n3Yvg7/Z+tCB9YLspmoYPl/2KVtHGoOBq43fVIjgAa2zWpbrg3nR14e53IUWKX393\nAZ3OQVkaP2bClQUKlSMjqFYWMWsggXOqx7Y9bvN3aIOQLs6+TN9iXaVa4wizcyD1\nsbKaL2nmFd5fnp8BU5kHs28=\n-----END PRIVATE KEY-----\n",
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