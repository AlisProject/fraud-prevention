Protect ICO projects from scammers.
===
  
[![ALIS](./images/logo.png)](https://alismedia.jp)
  
Be careful.  
Scammers REALLY likes ICO project.  

# Slackbot reminder scam
The Slackbot reminder scam is very popular fraud in ICO project.  
    
- [You can check detail here.](https://medium.com/@alismedia/how-to-determine-if-ico-projects-are-dangerous-chapter-team-administration-first-part-4e0abbc76d3d) 

Maybe almost every project has this scam experience.   
To prevent this scam, we wrote short python script with Slack API.   
This script send `/reminder` commands with warning messages to all of Slack team members. 

![](./images/for-slackbot-scam.png)  
  
##### Usage
1. You can get a Slack API token from [here](https://api.slack.com/custom-integrations/legacy-tokens). 
1. `export ALIS_FRAUD_PREVENTION_SLACK_API_TOKEN=xoxp-1234-YOUR-TOKEN-HERE` 
1. `git clone https://github.com/AlisProject/fraud-prevention.git`
1. `cd fraud-prevention`
1. `pip install slackclient` 
1. `python ./slackbot-resistant/index.py`

#### For new members
For protect new members of Slack team from Slackbot reminder scam, 
we made another script using AWS lambda and CloudWatch event.  
  
The script send similar message  in 1 minuit when new member joined in Slack team.  
This script depends `pip` and `aws-cli`. 

1. Create AWS Lambda function as `slackBotMessageForNewMember` by `python2.7`
    - ex: 
    
            aws lambda create-function \
            --function-name "slackBotMessageForNewMember" \
            --runtime "python2.7" \
            --role ... \
            --handler index.py
1. `git clone https://github.com/AlisProject/fraud-prevention.git`
1. `cd fraud-prevention`
1. `pip install SlackClient -t ./slackbot-for-new-member`
1. `cd slackbot-for-new-member`
1. `zip -r slackbot-for-new-member.zip ./*`
1. `cd ..`
1. Upload to AWS Lambda. 

        aws lambda update-function-code \
        --function-name slackBotMessageForNewMember \
        --zip-file fileb://slackbot-for-new-member/slackbot-for-new-member.zip

1. Set lambda environment valuable `token` as Slack API token.
1. Set CloudWatch Event to execute above in 1 minuit each.

## Fishing on Slack
Also, fishing on Slack is very common fraud in ICO project.  
For example, Ethereum address is only 42 characters text.
- ex: `0xEA610B1153477720748DC13ED378003941d84fAB`  

It is very easy to trick someone.  
Just type fishing ETH address to ICO project's Slack channel.  
That's all. [And get lots of money](http://thehackernews.com/2017/08/enigma-cryptocurrency-hack.html).

So we made simple chat-bot using [botkit](https://github.com/howdyai/botkit) and [heroku](https://herokuapp.com/).  
When someone type ETH address, this bot send message like that:

![](./images/fishing-on-slack.png)

Is it perfect way? No.  
However I think it is enough to prevent this fraud.

##### Usage
Depends `yarn` or `npm` and `heroku` cli tool.  
If you need 24 hours protection, you should pay monthly fee to heroku.

1. `git clone https://github.com/AlisProject/fraud-prevention.git`
1. `cd fraud-prevention`
1. `yarn`
1. Create bot integration at Slack [here](https://my.slack.com/services/new/bot).
    - and get API Token.
1. `heroku login` 
1. `git push heroku master` 
1. `heroku config:add token=YOUR_SLACK_API_TOKEN`
1. Turn on the **worker** on heroku.
