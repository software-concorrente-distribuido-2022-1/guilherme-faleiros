import json
from uuid import uuid4
from base_client import BaseClient

consumer = BaseClient(3000, 1024)

for _ in range(10):
    id = uuid4()
    response = consumer.send_message(json.dumps({ 'event_type': 'CONSUME', 'id': str(id), 'message': f"MESSAGE-{str(id)}" }))
    print(response)