/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           ______     ______     ______   __  __     __     ______
          /\  == \   /\  __ \   /\__  _\ /\ \/ /    /\ \   /\__  _\
          \ \  __<   \ \ \/\ \  \/_/\ \/ \ \  _"-.  \ \ \  \/_/\ \/
           \ \_____\  \ \_____\    \ \_\  \ \_\ \_\  \ \_\    \ \_\
            \/_____/   \/_____/     \/_/   \/_/\/_/   \/_/     \/_/


This is a sample Slack bot built with Botkit.

This bot demonstrates many of the core features of Botkit:

* Connect to Slack using the real time API
* Receive messages based on "spoken" patterns
* Reply to messages
* Use the conversation system to ask questions
* Use the built in storage system to store and retrieve information
  for a user.

# RUN THE BOT:

  Get a Bot token from Slack:

    -> http://my.slack.com/services/new/bot

  Run your bot from the command line:

    token=<MY TOKEN> node slack_bot.js

# USE THE BOT:

  Find your bot inside Slack to send it a direct message.

  Say: "Hello"

  The bot will reply "Hello!"

  Say: "who are you?"

  The bot will tell you its name, where it is running, and for how long.

  Say: "Call me <nickname>"

  Tell the bot your nickname. Now you are friends.

  Say: "who am I?"

  The bot will tell you your nickname, if it knows one for you.

  Say: "shutdown"

  The bot will ask if you are sure, and then shut itself down.

  Make sure to invite your bot into other channels using /invite @<my bot>!

# EXTEND THE BOT:

  Botkit has many features for building cool and useful bots!

  Read all about it here:

    -> http://howdy.ai/botkit

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/


if (!process.env.token) {
    console.log('Error: Specify token in environment');
    process.exit(1);
}

var Botkit = require('botkit');

var controller = Botkit.slackbot({
    debug: true
});

var bot = controller.spawn({
    token: process.env.token
}).startRTM();

var warning_message = ":warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:";
warning_message += "\nPlease be aware of fraud! We will *NEVER* give you the ICO's ETH address via Slack!";
warning_message += "\n詐欺に気をつけてください！ ALISチームがSlack上でICO用のETHアドレスを書くことは *絶対にありません* !";
warning_message += "\n请小心诈骗！此外，绝对不要在Slack上发布ICO的任何以太坊地址！";
warning_message += "\n\nSorry, ETH address is not accepted because of fraud prevention.";
warning_message += "\n申し訳ありませんが、詐欺防止のためETHアドレスは禁止とさせていただいております。";
warning_message += "\nETH地址禁止防止欺诈！";
warning_message += "\n:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:";

controller.hears(['0x[0-9a-f]{20}'], 'ambient, message_received', function(bot, message) {
  bot.reply(message, warning_message);
});
