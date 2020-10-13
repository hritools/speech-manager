## Prerequisites
* Python 3.6+

## Set up
```bash
sudo apt install rabbitmq-server
pip install -Ur requirements.txt
cp src/.env-example src/.env
```

## Launch (dev)
`$ sudo rabbitmq-server`  
`$ celery -A tasks worker -B`  
`$ python server.py`


## Configuration
Configuration is stored in .env file.  
### Parameters
#### `TTS_SOURCE`
Options:
* `web` (requests to TTS web service)
* `local` (using local RHVoice. [More on Wiki](https://cordelianew.university.innopolis.ru/wiki/doku.php?id=rhvoice).)

#### `BROKER_URL`
Broker is used by Celery. [Read more..](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)