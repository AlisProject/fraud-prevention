# -*- coding: utf-8 -*-
import os
import sys
from slackclient import SlackClient

slack_token = os.environ["ALIS_FRAUD_PREVENTION_SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

message = u'''
Please be aware of Slackbot fraud! If you receive any messages from Slackbot, *it best to treat them as fraudulent at first* . 
Slackbot詐欺に気を付けてください！ *Slackbotからのメッセージはすべて詐欺と考えてください。*
请注意来自Slackbot的虚假信息！*所有来自Slackbot的信息均为虚假信息！*

We will *NEVER* give you the ICO's ETH address via Slack! 
また、Slack上でICO用のETHアドレスを書くことは *絶対にありません* !
此外，绝对不要在Slack上发布ICO的任何以太坊地址！
'''

# Get all users
users = sc.api_call(
  "users.list"
)

# Add reminders.
for user in users["members"]:
  sc.api_call(
    "reminders.add",
    text=message.encode('utf-8') ,
    time=sys.argv[1], # Unix timestamp.
    user=user['id']
  )
  print user['name'] + ' ' + user['id']
