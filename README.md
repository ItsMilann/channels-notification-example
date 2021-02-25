### Simple Notification
A basic & minimal example, of handling notification using websocket.

### Tools
- [Django 3.1](https://djangoproject.com)
- [Channels 3.0.1](https://channels.readthedocs.io/en/stable/)

### Installation

On your terminal/shell

```bash
git pull https://github.com/ItsMilann/channels-notification-example.git

pip3 install -r requirements.txt

sudo docker run -p 6379:6379 -d redis:5

./ manage.py migrate

./ manage.py runserver
```