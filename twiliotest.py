import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACfd2ff4430b3e7b92526cf447d3aff48c'
auth_token = '7209667823a273db71e0865965e33e52'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='\r \r This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+19285758326',
         to='+13147554809'
     )

print(message.sid)