import os
import firebase_admin
import json

from dotenv.main import load_dotenv
from firebase_admin import firestore


load_dotenv()

def get_config():
    project_id = os.environ.get("PROJECT_ID")
    certificate_file = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not certificate_file:
        return
    
    with open(certificate_file, "r") as key_file:
        json_keys = json.load(key_file)
        api_key = json_keys.get("private_key")
    
    return {
        "apiKey": f"{api_key}",
        "authDomain": f"{project_id}.firebaseapp.com",
        "databaseURL": f"https://{project_id}.firebaseio.com",
        "storageBucket": f"{project_id}.appspot.com",
        "serviceAccount": f"{certificate_file}"
    }


def get_default_or_initialize_app():
    if firebase_admin._apps:
        return firebase_admin.get_app()
    
    config = get_config()
    if config:
        cred = firebase_admin.credentials.Certificate(config.get('serviceAccount')) 
        return firebase_admin.initialize_app(cred, {'storageBucket': f'{config.get("storageBucket")}'})
    
    raise Exception("Config not found")


def get_data_from_database():
    app = get_default_or_initialize_app()
        
    fireclient = firestore.client()
    coll_ref = fireclient.collection(u'objetos-scraping')
    docs = coll_ref.stream()
    
    return docs


def get_filtered_data():    
    data_docs = get_data_from_database()
    filtered_data = {}
    for data in data_docs:
        data_id = data.id
        _data = data.to_dict().get("dc")
        filtered_data.update({
            data_id: {
                "title": _data.get("title"),
                "subject": _data.get("subject"),
                "source": _data.get("source"),
                "description": _data.get("description"),
            }
        })
    return filtered_data
