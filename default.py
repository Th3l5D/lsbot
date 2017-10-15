import socket
import plugin
import ssl
import user
import os

class bot(object):

    def __init__(self, server):
        self.server = server
        self.port = 6667
        self.ssl = None
        self.channels = []
        self.connectedChannels = []
        self.nick = 'default_nick'
        self.realName = 'default_nick default_nick'
        self.socket = None
        self.debugger = True
        self.allowedCommands = {
            'ping': self.ping, 'privmsg': self.privmsg, 'invite': self.invite,
            'join': self.join, '433': self.f433, '307':self.f307, '353':self.f353}
        self.autoInvite = True
        self.plugins = plugin.Plugin(self.rawSend)
        self.userlist = {}

    def debug(self, line):
        if self.debugger is not None:
            print(line)

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.ssl is not None:
            self.socket = ssl.wrap_socket(self.socket)
        self.socket.connect((self.server, self.port))
        self.authenticate()
        
    def authenticate(self):
        self.rawSend('NICK', self.nick)
        self.rawSend('USER', ' '.join((self.nick, self.nick, self.realName)))

    def joinChannel(self, channel = None):
        if channel is not None:
            self.channels.append(channel)
        for chan in self.channels:
            if chan not in self.connectedChannels:
                self.rawSend('JOIN', chan)
                self.connectedChannels.append(chan)

    def rawSend(self, command, content, dest = ''):
        line = ' '.join((command, dest, content, '\r\n'))
        self.debug(line)
        self.socket.send(bytes(line, 'UTF-8'))

    def splitLine(self, line):
        datas_dict = {}
        if line.startswith(':'):
            datas_dict['from'], line = line[1:].split(' ', 1)
            datas_dict['from'] = datas_dict['from'].split('!')[0]

        datas = line.split(' ', 1)
        datas_dict['command'] = datas[0]
        if datas_dict['command'].isdigit():
        # numeric commands are server response and don't follow any logic. annoying :/
        # so we just put the whole line into content. Parsing is done in functions
            datas_dict['content'] = datas[1]
        else:
            splited = datas[1].split(':', 1)
            if len(splited) > 1:
                datas_dict['to'] = splited[0].strip()
                datas_dict['content'] = splited[1]
            else:
                datas_dict['to'], datas_dict['content'] = splited[0].split(' ', 1)


        return datas_dict

    def parseLine(self, line):
        self.debug(line)
        datas = self.splitLine(line)
        self.debug(datas)
        if datas['command'].lower() in self.allowedCommands.keys():
            self.allowedCommands[datas['command'].lower()](datas)

        if datas['command'] == 'MODE':
            self.joinChannel()

        pass

    def listen(self):
        queue = ''
        while(1):
            raw = self.socket.recv(1024).decode('UTF-8', 'replace')
            queue = ''.join((queue, raw))
            splited = queue.split('\r\n')
            if len(splited) > 1:
                for line in splited[:-1]:
                    self.parseLine(line)
            queue =  splited[-1]
        

    # received commands

    def ping(self, datas):
        self.rawSend('PONG', datas['content'])

    def invite(self, datas):
        if self.autoInvite:
            self.joinChannel(datas['content'])

    def privmsg(self, datas):
        if(datas['to'] not in self.connectedChannels):
            for chan in self.connectedChannels:
                self.rawSend('PRIVMSG', ', '.join((datas['from'], 'il veut violer mon intimité.')), chan)
        else:
            # get first word, to check if it's a plugin
            word = datas['content'].split(' ', 1)[0]
            if(word.startswith('!') and word[1:].isalnum()):
                self.plugins.execute(datas, self.userlist)

    def join(self, datas):
        self.whois(datas['from'])


    def f433(self, datas):
        # nickname is already in use.
        self.debug('nick utilise. Adding a _')
        b.nick = b.nick+'_'
        self.authenticate()

    def f307(self, datas):
        # user is identified
        user = datas['content'].split()[1]
        self.userlist[user].identified = True
        self.debug(self.userlist)

    def f353(self, datas):
        # list users connected to a channel
        users = datas['content'].split(':')[1].split()
        for user in users:
            self.whois(user)


    # send commands
    def whois(self, username):
        self.rawSend('WHOIS', '', username)
        self.userlist[username] = user.user(username)



conf_file = open(os.path.dirname(os.path.realpath(__file__))+'/config.ini').readlines()
config = {}
for line in conf_file:
    if line.strip()[0] is not '#':
        splited = line.split('=', 1)
        config[splited[0].strip()] = splited[1].strip()

b = bot(config['server'])
b.nick=config['nick']
b.ssl = config['ssl']
b.port = int(config['port'])
for chan in config['channels'].split(','):
    b.channels.append(chan.strip())
b.connect()
b.listen()
