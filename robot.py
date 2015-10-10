import twitch
import serial
import json


t = twitch.Twitch();
 
username = "username_here";
key = "oauth_token_here";
# Get your oauth token here -> http://www.twitchapps.com/tmi/

t.twitch_connect(username, key);

ser = serial.Serial('/dev/ttyACM1', 9600)

while True:
  new_messages = t.twitch_recieve_messages();
 
  if not new_messages:
    continue
  else:
    for message in new_messages:
      msg = message['message']
      username = message['username']
      action = {
        "type": msg
      }
      res = json.dumps(action)
      ser.write(res)
      print(action)