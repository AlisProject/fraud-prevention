# -*- coding: utf-8 -*-
import os
import sys
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


给新会员: *请注意来自Slack的虚假信息！*

- 请注意来自Slackbot的虚假信息！*所有来自Slackbot的信息均为虚假信息！*
- 此外，绝对不要在Slack上发布ICO的任何以太坊地址！
- 请将 *所有的私人消息视为欺诈消息* ！！！
- 所有 *预售招标是欺诈！！！*

:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:
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
