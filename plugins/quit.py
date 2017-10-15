import glob
import os
import sys


class quit:
    def __init__(self, rawSend):
        self.rawSend = rawSend

    def execute(self, **kwargs):
        datas = kwargs['datas']
        users = kwargs['users']

        if 'Th3_l5D' == datas['from'] or 'the_lsd' == datas['from']:
            if users[datas['from']].identified:
                self.rawSend('PRIVMSG', 'kthxbye', datas['to'])
                self.rawSend('QUIT', 'J\'vais aller faire les courses')
                sys.exit()
            else:
                self.rawSend('PRIVMSG',  'Psst, hey, pssst, t\'es pas VRAIMENT mon maitre en fait !', datas['to'])

        else:
            self.rawSend('PRIVMSG',  datas['to'], 'Prend moi pour un jambon!')

