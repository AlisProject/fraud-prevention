Protect ICO projects from scammers.

# Usage

## For Slackbot scam
1. You can get a Slack API token from [here](https://api.slack.com/custom-integrations/legacy-tokens). 
1. `export ALIS_FRAUD_PREVENTION_SLACK_API_TOKEN=xoxp-1234-YOUR-TOKEN-HERE` 
1. `pip install slackclient` 
1. `python ./slackbot-resistant/index.py 1503301170`
    - `1503301170` is Unix timestamp of notify message. Please change it.

## For Slack scam
Specify `Restrict API Token Usage` is recommended at Slack bot integration settings.

1. `yarn`
1. Create bot integration.
    - https://my.slack.com/services/new/bot
