from Args   import Args
from Slack  import Slack
from Teleg  import Teleg
from Server import Server


teleg  = Teleg (Args["TELEG_BOT_ID"],Args["TELEG_CHAT_ID"])
slack  = Slack (Args["SLACK_TOKEN" ],Args["SLACK_CHANNEL"])
server = Server(teleg,slack)
