from slackclient import SlackClient
from time        import time


class Slack():
    def __init__(self,token,channel):
        self.conn = SlackClient(token)
        self.channel = channel
        self.oldest = int(time())
        self.users = {}
    def rx(self):
        messages = []
        try:
            resp = self.conn.api_call("channels.history",channel=self.channel,oldest=self.oldest)
            assert resp["ok"]
            for message in resp["messages"]:
                try:
                    self.oldest = max(self.oldest,int(float(message["ts"]))+1)
                    messages.append({"from":self.getUser(message["user"]),"text":message["text"]})
                except:
                    pass
        except:
            pass
        return messages
    def tx(self,username,text):
        message = {}
        try:
            resp = self.conn.api_call("chat.postMessage",channel=self.channel,username=username,text=text)
            assert resp["ok"]
            try:
                message = {"from":resp["message"]["username"],"text":resp["message"]["text"]}
            except:
                pass
        except:
            pass
        return message
    def getUser(self,user):
        if user not in self.users:
            resp = self.conn.api_call("users.info",user=user)
            assert resp["ok"]
            self.users[user] = resp["user"]["name"]
        return self.users[user]
