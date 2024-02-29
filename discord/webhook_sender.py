import requests


def send_webhook(url, name, content):
    data = {
        'username': name,
        'content': content,
    }

    requests.post(url, json=data)

