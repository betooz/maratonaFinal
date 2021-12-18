import sys
import requests

def send():
    params = {
        "email": "daniel.ortiz.bernal@gmail.com",
        "assistantId": "5a80311f-4741-4da9-a8d8-9dea75c4f982",
        "url": "https://api.us-south.assistant.watson.cloud.ibm.com/instances/705f9c82-2fea-4add-b4fc-3417b9d3b475/v2/assistants/5a80311f-4741-4da9-a8d8-9dea75c4f982/sessions",
        "skillId": "e2d207ec-1551-412c-9c5a-d306e7c0a48c",
        "apiKey": "CHua3AcpykpIvWowMlrTTxhYDnc3aMd4jVepzBhoruKN",
        "submitConfirmation": True
    }
    url = "http://172.21.188.211:3000/submit"
    respond = requests.post(url, data=params)
    print(respond)
    print(respond.text)
    print(respond.json())