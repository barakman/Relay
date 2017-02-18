In order to relay messages between a Slack channel and a Telegram room, you need the following:

1. SLACK_TOKEN:
   - Generate a token for the Slack channel at https://api.slack.com/docs/oauth-test-tokens

2. SLACK_CHANNEL:
    - Retrieve the ID of the Slack channel

3. TELEG_BOT_ID:
   Create a bot in the Telegram room:
   - Enter /newbot and ollow the instructions given by the BotFather
   - Enter /setprivacy and disable the bot's privacy
   You can read more detailed instructions at either one of the following:
   - https://core.telegram.org/bots#6-botfather 
   - http://botsfortelegram.com/project/the-bot-father/

4. TELEG_CHAT_ID:
   - Retrieve the ID of the chat in the Telegram room

In order to relay messages using webhooks instead of polling, you also need the following:

5. SLACK_WEBHOOK:
   - Obtain an https url for your server
   - Create a webhook between the Slack channel and your server (at https://my.slack.com/services/new/outgoing-webhook)

6. SLACK_PORT_ID:
   - Open a designated port on your server

7. TELEG_WEBHOOK:
   - Obtain an https url for your server
   - Create a webhook between the Telegram room and your server (read more at https://core.telegram.org/bots/webhooks)

8. TELEG_PORT_ID:
   - Open a designated port on your server

When done, paste each one of the arguments that you have acquired into the configuration file.
