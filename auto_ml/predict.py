import sys
import os
import keys
import json
from google.cloud import automl_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CodeChella-315303cc6526.json'
# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CodeChella-315303cc6526.json'
    prediction_client = automl_v1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name=name, payload=payload)
    json_string = type(request).to_json(request)
    jsn = json.loads(json_string)
    return(jsn['payload'][0]['displayName'])  # waits till request is returned

"""
if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CodeChella-315303cc6526.json'

    file_path = sys.argv[1]
    project_id = sys.argv[2]
    model_id = sys.argv[3]

    with open(file_path, 'rb') as ff:
        content = ff.read()

    x = get_prediction(content, project_id, model_id)
    print (x)
"""
