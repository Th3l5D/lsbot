import glob
import os
import sys


class quit:
	def __init__(self, rawSend):
		self.rawSend = rawSend

	def execute(self, datas):
		if 'Th3_l5D' == datas['from'] or 'the_lsd' == datas['from'] :
			self.rawSend('PRIVMSG',  datas['to'], 'NOP !')
			sys.exit()
		else:
			self.rawSend('PRIVMSG',  datas['to'], 'Prend moi pour un jambon!')

