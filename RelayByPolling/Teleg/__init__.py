from urllib  import urlencode
from urllib2 import urlopen
from json    import loads


class Teleg():
    def __init__(self,bot_id,chat_id):
        self.bot_id = bot_id
        self.chat_id = chat_id
        self.offset = 0
        conn = urlopen("https://api.telegram.org/bot"+self.bot_id+"/deleteWebhook")
        data = conn.read()
        resp = loads(data)
        conn.close()
        assert resp["ok"]
    def rx(self):
        messages = []
        try:
            args = {"offset":self.offset}
            conn = urlopen("https://api.telegram.org/bot"+self.bot_id+"/getUpdates",urlencode(args))
            data = conn.read()
            resp = loads(data)
            conn.close()
            assert resp["ok"]
            for result in resp["result"]:
                try:
                    self.offset = max(self.offset,result["update_id"]+1)
                    messages.append({"from":self.getUser(result["message"]["from"]),"text":result["message"]["text"]})
                except:
                    pass
        except:
            pass
        return messages
    def tx(self,username,text):
        message = {}
        try:
            args = {"chat_id":self.chat_id,"text":"["+ascii(username)+"] says: "+ascii(text)}
            conn = urlopen("https://api.telegram.org/bot"+self.bot_id+"/sendMessage",urlencode(args))
            data = conn.read()
            resp = loads(data)
            conn.close()
            assert resp["ok"]
            try:
                message = {"from":resp["result"]["from"]["first_name"],"text":resp["result"]["text"]}
            except:
                pass
        except:
            pass
        return message
    def getUser(self,user):
        return ascii(user["first_name"])+" "+ascii(user["last_name"]) if "last_name" in user else user["first_name"]


def ascii(string):
    return string if isinstance(string,str) else string.encode("utf-8")
