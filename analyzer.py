import os

from dotenv.main import load_dotenv
from google.oauth2 import service_account
from google.cloud import language_v1

from utils import DATA_CLASSES

load_dotenv()

cred = service_account.Credentials.from_service_account_file(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_NLP"))
client = language_v1.LanguageServiceClient(credentials=cred)
document_type = language_v1.Document.Type.PLAIN_TEXT
encoding_type = language_v1.EncodingType.UTF8


def classify_text(text_content):
    document = {"content": text_content, "type_": document_type, }

    content_categories_version = (
        language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
    )

    response = client.classify_text(
        request={
            "document": document,
            "classification_model_options": {
                "v2_model": {"content_categories_version": content_categories_version}
            },
        }
    )

    categories = {}
    for category in response.categories:
        if category.name in DATA_CLASSES and category.confidence > 0.5:
            categories.update({category.name: category.confidence})
    
    return categories


def analyze_completeness(data, expected_keys):
    total_fields = len(expected_keys)
    filled_fields = []
    missing_fields = []

    for key in expected_keys:
        nested_keys = key.split('.')
        value = data
        for nested_key in nested_keys:
            if nested_key in value:
                value = value[nested_key]
            else:
                missing_fields.append(key)
                break
        else:
            if value:
                filled_fields.append(key)
            else:
                missing_fields.append(key)

    completeness = (len(filled_fields) / total_fields)

    return {
        "completeness": completeness,
        "filled_fields": filled_fields,
        "missing_fields": missing_fields
    }