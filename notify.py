import requests
import json

def notify(msg):
    serverToken = 'AIzaSyDNmfAYnsmJDn6Bb0QIIzMvfciEume8oWY'
    deviceToken = 'fsSIf8acbw0:APA91bFxeK-Ba-3_PxGWt_RPvmA3890vRxxqb7YlurxGjNsr0zDD42shV07eZaBV8-FPHWlSPqe4y8OPTfNIx--AaJXlURUNrIwECX4alzi0wqm8hnITGRqxe33WXS6pikkv-lNmDcyX'
    senderid = "notification-40514"

    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
            'Sender':senderid
      }

    body = {
         'notification':
             {
                 'header': 'Elderly assistance',
                 'body': msg,
                 'location':'72.4345,12.234897',
                 'type':'map'
          },
          'priority': 'high',
          'to':deviceToken
        }

    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())

