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
warning_message += "\n\nSorry, ETH address is not accepted because of fraud prevention.";
warning_message += "\n申し訳ありませんが、詐欺防止のためETHアドレスは禁止とさせていただいております。";
warning_message += "\n:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:";

controller.hears(['0x[0-9a-f]{20}'], 'ambient, message_received', function(bot, message) {
  bot.reply(message, warning_message);
});
