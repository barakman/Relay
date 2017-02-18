from urllib  import urlencode
from urllib2 import urlopen
from json    import loads


class Teleg():
    def __init__(self,bot_id,chat_id,webhook=""):
        self.bot_id = bot_id
        self.chat_id = chat_id
        if webhook:
            args = {"url":webhook}
            conn = urlopen("https://api.telegram.org/bot"+self.bot_id+"/setWebhook",urlencode(args))
            data = conn.read()
            resp = loads(data)
            conn.close()
            assert resp["ok"]
    def rx(self,data):
        result = loads(data)
        return {"from":self.getUser(result["message"]["from"]),"text":result["message"]["text"]}
    def tx(self,username,text):
        args = {"chat_id":self.chat_id,"text":"["+ascii(username)+"] says: "+ascii(text)}
        conn = urlopen("https://api.telegram.org/bot"+self.bot_id+"/sendMessage",urlencode(args))
        data = conn.read()
        resp = loads(data)
        conn.close()
        assert resp["ok"]
        return {"from":resp["result"]["from"]["first_name"],"text":resp["result"]["text"]}
    def getUser(self,user):
        return ascii(user["first_name"])+" "+ascii(user["last_name"]) if "last_name" in user else user["first_name"]


def ascii(string):
    return string if isinstance(string,str) else string.encode("utf-8")
