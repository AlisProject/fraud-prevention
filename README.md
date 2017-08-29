Protect ICO projects from scammers.

# Usage

## For Slackbot scam
1. You can get a Slack API token from [here](https://api.slack.com/custom-integrations/legacy-tokens). 
1. `export ALIS_FRAUD_PREVENTION_SLACK_API_TOKEN=xoxp-1234-YOUR-TOKEN-HERE` 
1. `pip install slackclient` 
1. `python ./slackbot-resistant/index.py 1503301170`
    - `1503301170` is Unix timestamp of notify message. Please change it.

### Fro new member
Depends `pip` and `aws-cli`. 

1. Create AWS Lambda function as `slackBotMessageForNewMember` by `python2.7`
    - ex: 
    
            aws lambda create-function \
            --function-name "slackBotMessageForNewMember" \
            --runtime "python2.7" \
            --role ... \
            --handler index.py
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

## For Slack scam
Specify `Restrict API Token Usage` is recommended at Slack bot integration settings.

1. `yarn`
1. Create bot integration.
    - https://my.slack.com/services/new/bot

