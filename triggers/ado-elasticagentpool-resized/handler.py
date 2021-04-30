from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging
import json

relay = Interface()
app = Quart('ado-pullrequest-merged')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    payload = await request.get_json()
    ado_event = payload.body.get('eventType')

    if ado_event is None:
        return {'message': 'Not a valid Azure Devops event'}

    if ado_event != "git.pullrequest.merged":
        return {'message': 'only git.pullrequest.merged events are supported by this trigger'}
     
    logging.info("Received event from azure devops: {}".format(ado_event))
    logging.info("Received the following webhook payload: \n%s", json.dumps(payload, indent=4))

    resource = payload['resource']

    if resource['mergeStatus'] == "succeeded" and resource['status'] == "status":
        relay.events.emit({
            'url': resource['url'],
            'repositoryURL': resource['repository']['url'],
            'sourceRefName': resource['repoistory']['sourceRefName'],
            'targetRefName': resource['repository']['targetRefName']
        })
    return {'message': 'success'}, 200, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()