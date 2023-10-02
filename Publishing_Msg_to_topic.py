## To Publish message to PubSup Topic

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
    record = json.load(file)
    final = json.dumps(record)

    print(final)
    print(record,'\n')


#data1= bytearray(record)
#print(data1)

data = final.encode('utf-8')

#data1= bytearray(data)
#print(data1)

print(data)
future = publisher.publish(topic_path, data)

print(future.result())

