import os

from google.cloud import pubsub_v1

project_id = os.environ.get('GCP_PROJECT_ID')
topic_id = "my-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 10):
    data_str = f"Message number {n}"

    data = data_str.encode("utf-8")

    future = publisher.publish(topic_path, data)
    print(future.result())

print(f"Published messages to {topic_path}.")
