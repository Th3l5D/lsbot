class io(object):
    """docstring for io"""
    def __init__(self, rawSend):
        self.rawSend = rawSend

    def execute(self, datas):
        self.rawSend('PRIVMSG', 'Saaalut, '+datas['from'],  datas['to'])

