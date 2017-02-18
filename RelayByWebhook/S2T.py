from Args   import Args
from Slack  import Slack
from Teleg  import Teleg
from Server import Server


slack  = Slack (Args["SLACK_TOKEN"  ],Args["SLACK_CHANNEL"],Args["SLACK_WEBHOOK"])
teleg  = Teleg (Args["TELEG_BOT_ID" ],Args["TELEG_CHAT_ID"])
server = Server(Args["SLACK_PORT_ID"],slack,teleg)
