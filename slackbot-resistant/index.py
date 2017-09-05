# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime
from slackclient import SlackClient

slack_token = os.environ["ALIS_FRAUD_PREVENTION_SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

message = u'''
:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:

*Please be aware of fraud on Slack.*
    
- Please be aware of Slackbot fraud! If you receive any messages from Slackbot, *it best to treat them as fraudulent at first* . 
- We will *NEVER* give you the ICO's ETH address via Slack! 
- Please think like that: *Every direct messages are fraud!!!!!*
- All of *PreSale information is fraud!!!*
- Please *NEVER CLICK FISHY LINKS!!!*


*Slackでの詐欺にお気をつけください。*

- Slackbot詐欺に気を付けてください！ *Slackbotからのメッセージはすべて詐欺と考えてください。*
- Slack上でICO用のETHアドレスを書くことは *絶対にありません* !
- *すべてのダイレクトメッセージは詐欺* と考えてください！！！
- *すべてのプリセールの勧誘は詐欺* です！！！
- *怪しいリンクは決して不用意にクリックしないでください！！！*
:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:
'''

# Get all users
users = sc.api_call(
  "users.list"
)

# Add reminders.
index = 0
interval = 6
remindTime = int(datetime.now().strftime("%s")) + 600 # 10 minutes from execute.
for user in users["members"]:
  index += 1

  # exclude bot users.
  if user['is_bot'] or user['id'] == 'USLACKBOT':
    continue

  time.sleep(interval)
  remindTime += interval
  result = sc.api_call(
    "reminders.add",
    text=message.encode('utf-8') ,
    time=remindTime,
    user=user['id']
  )
  print str(index) + ': ' + user['name'] + ' ' + user['id'] + ': ' + str(result['ok'])

