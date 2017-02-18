from slackclient import SlackClient
from urlparse    import parse_qs


class Slack():
    def __init__(self,token,channel,webhook=""):
        self.conn = SlackClient(token)
        self.channel = channel
        self.users = {}
    def rx(self,data):
        message = parse_qs(data)
        return {"from":self.getUser(message["user_id"][0]),"text":message["text"][0]}
    def tx(self,username,text):
        resp = self.conn.api_call("chat.postMessage",channel=self.channel,username=username,text=text)
        assert resp["ok"]
        return {"from":resp["message"]["username"],"text":resp["message"]["text"]}
    def getUser(self,user):
        if user not in self.users:
            resp = self.conn.api_call("users.info",user=user)
            assert resp["ok"]
            self.users[user] = resp["user"]["name"]
        return self.users[user]
