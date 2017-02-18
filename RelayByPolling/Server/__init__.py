def Server(src,dst):
    while True:
        for message in src.rx():
            log("RX",message)
            log("TX",dst.tx(message["from"],message["text"]))


def log(prefix,message):
    if message:
        print prefix+" ["+ascii(message["from"])+": "+ascii(message["text"])+"]"


def ascii(string):
    return string if isinstance(string,str) else string.encode("utf-8")
