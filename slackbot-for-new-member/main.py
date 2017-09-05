# -*- coding: utf-8 -*-
import os
from datetime import datetime
from slackclient import SlackClient

slack_token = os.environ["ALIS_FRAUD_PREVENTION_SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

message = u'''
:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:

For the new member: *Please be aware of fraud on Slack.*
    
- Please be aware of Slackbot fraud! If you receive any messages from Slackbot, *it best to treat them as fraudulent at first* . 
- We will *NEVER* give you the ICO's ETH address via Slack! 
- Please think like that: *Every direct messages are fraud!!!!!*
- All of *PreSale information is fraud!!!*


新しくALISのSlackに登録された方へ: *Slackでの詐欺にお気をつけください。*

- Slackbot詐欺に気を付けてください！ *Slackbotからのメッセージはすべて詐欺と考えてください。*
- Slack上でICO用のETHアドレスを書くことは *絶対にありません* !
- *すべてのダイレクトメッセージは詐欺* と考えてください！！！
- *すべてのプリセールの勧誘は詐欺* です！！！
:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:
'''


def main_handler(event, context):
    # Get all users
    users = sc.api_call(
        "users.list"
    )

    # Add reminders.
    current_timestamp = int(datetime.now().strftime("%s"))
    in10minutes = current_timestamp - 60
    for user in users["members"]:
        if user['updated'] >= in10minutes:
            sc.api_call(
                "reminders.add",
                text=message.encode('utf-8'),
                time=current_timestamp + 60,
                user=user['id']
            )
            print user['name'] + ' ' + user['id']
