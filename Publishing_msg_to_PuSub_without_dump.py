
from google.cloud import pubsub_v1
import json
import argparse

project = "sre-project-397019"
topic_name = "demo"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project, topic_name)

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

with args.file as file:
    record = str(json.load(file))
    print(record)



data = record.encode('utf-8')
print(data)
future = publisher.publish(topic_path, data,origin="python-sample", username="gcp")

print(future.result())
