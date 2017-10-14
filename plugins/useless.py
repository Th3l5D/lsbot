import random

""" usage useless : donne un site web inutile au hasard. Utilisation !useless """

class useless:

    def __init__(self, rawSend):
        self.rawSend = rawSend

    def execute(self, datas):

        self.sites = 'http://heeeeeeeey.com/ http://thatsthefinger.com/ http://cant-not-tweet-this.com/ http://eelslap.com/ http://www.staggeringbeauty.com/ http://burymewithmymoney.com/ http://www.fallingfalling.com/ http://ducksarethebest.com/ http://www.trypap.com/ http://www.republiquedesmangues.fr/ http://www.movenowthinklater.com/ http://www.partridgegetslucky.com/ http://www.rrrgggbbb.com/ http://beesbeesbees.com/ http://www.sanger.dk/ http://breakglasstosoundalarm.com/ http://www.koalastothemax.com/ http://www.everydayim.com/ http://www.leduchamp.com/ http://www.geodu.de/ http://grandpanoclothes.com/ http://www.haneke.net/ http://r33b.net/ http://randomcolour.com/ http://cat-bounce.com/ http://www.sadforjapan.com/ http://isitchristmas.com/ http://www.taghua.com/ http://chrismckenzie.com/ http://hasthelargehadroncolliderdestroyedtheworldyet.com http://ninjaflex.com/ http://iloveyoulikeafatladylovesapples.com http://ihasabucket.com/ http://corndogoncorndog.com/ http://giantbatfarts.com/ http://www.ringingtelephone.com/ http://www.pointerpointer.com/ http://www.pleasedonate.biz/ http://imaninja.com/ http://willthefuturebeaweso.me/ http://salmonofcapistrano.com/ http://www.ismycomputeron.com/ http://www.ooooiiii.com/ http://www.wwwdotcom.com/ http://www.nullingthevoid.com/ http://www.muchbetterthanthis.com/ http://www.ouaismaisbon.ch/ http://iamawesome.com/ http://www.pleaselike.com/ http://crouton.net/ http://corgiorgy.com/ http://www.electricboogiewoogie.com/ http://www.nelson-haha.com/ http://www.wutdafuk.com/ http://unicodesnowmanforyou.com/ http://tencents.info/ http://intotime.com/ http://leekspin.com/ http://minecraftstal.com/ http://www.riddlydiddly.com/ http://www.patience-is-a-virtue.org/ http://whitetrash.nl/ http://www.theendofreason.com/ http://zombo.com http://secretsfornicotine.com/ http://pixelsfighting.com/ http://crapo.la http://baconsizzling.com/'
        self.sites = self.sites.split()
        alea = random.randint(0,len(self.sites)-1)
        self.rawSend('PRIVMSG', datas['to']+' :'+datas['from']+': '+self.sites[alea]+'\r\n')