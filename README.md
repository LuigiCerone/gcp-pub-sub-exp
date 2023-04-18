# Google Cloud Platform Pub/Sub Python SDK example

## How to run

### Setup GCP

```bash
gcloud init
gcloud services enable pubsub.googleapis.com
gcloud auth application-default login

# Create topic.
gcloud pubsub topics create my-topic

# Create subscription.
gcloud pubsub subscriptions create my-sub --topic my-topic
```

### Setup venv

Local environment is set up by using [make](https://www.gnu.org/software/make/) tool.

```bash
make
```

### Run

```bash
source venv/bin/activate
python publisher.py
python subscriber.py
```

## Credits

Code from [official Google documentation](https://cloud.google.com/pubsub/docs/publish-receive-messages-client-library?hl=en).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
