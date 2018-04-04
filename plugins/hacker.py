import hashlib


class hacker:
    def __init__(self, rawSend):
        self.rawSend = rawSend
        self.left_part  = []
        self.right_part = []
        self.initSentences()

    def initSentences(self):
        self.left_part  = ['L\'enfant maudit', 'L\'enfant terrible', 'L\'OVNI', 'Le saltimbanque', 'Le magicien',
'La réincarnation', 'La personification', 'L\'extra-terreste', 'Son altesse', 'Le seigneur',
'La flamme incandescente', 'L\'orage moucheté', 'L\'hydre bicéphale', 'Le dernier survivant',
'Le démon', 'Le grand gourou', 'Le grand Neptune', 'L\'origine', 'Sa majesté', 'Le héron majestueux',
'Le sorcier', 'Le Christ', 'La tempête de jade', 'La fausse patte', 'Le tigre de cristal',
'Le phénix flamboyant', 'Le dernier de la dynastie', 'L\'héritier', 'Le fourbe serpent',
'L\'insatiable fouine', 'Le Jean-Paul Sartre', 'Le Picasso', 'Le samouraï', 'L\'enfant béni',
'Le grand chef de la tribu', 'Le sage', 'L\'Ancien', 'La belette aguerrie', 'Les griffes',
'La morsure', 'La tornade', 'Le séisme', 'La pluie de cendres', 'Le chasseur impertinent',
'L\'inexorable étreinte', 'Le bâtard royal', 'L\'assassin efféminé', 'Le peintre', 'L\'herboriste',
'Le fabuleux créateur', 'L\'omniprésent esprit', 'Le Léviathan', 'L\'immortel', 'Le capitaine Jack Sparrow',
'L\'élégant milliardaire', 'L\'ineffable vérité', 'Le soubresaut salvateur', 'Le danseur aux lames',
'L\'archiduc', 'Le sheikh', 'L\'arme secrète', 'L\'Excalibur', 'Le troisième oeil', 'Le Dieu égyptien',
'Le détenteur de la puissance', 'L\'éternel champion', 'L\'inéquarissable renard', 'L\'indiscret étourneau',
'L\'orbe mirobolante', 'Le grand dragon', 'Le rescapé', 'Le destructeur', 'Le soldat chaotique',
'Asmodéus, destructeur', 'Le Walker Texas Ranger', 'Merlin, Grand Enchanteur', 'Le Serpentard',
'Le petit malin', 'L\'enfant rusé', 'Le sanguinaire', 'Le héros anonyme', 'L\'alchimiste',
'La perfection métabolique', 'Le choléra synergique', 'Le phénomène fuligineux',
'La loi de L\'échange équivalent', 'L\'ornythorinque incestueux', 'Le franc-maçon', 'L\'illuminati pyramidal',
'Le spectre oublié', 'Le loup de mer solitaire', 'Le chêne centenaire', 'Le scorpion opiniâtre',
'La libellule frénétique', 'Le passe-muraille', 'La vengance karmique', 'Le commandant des armées',
'Le génie calculateur', 'Le présage essentiem', 'L\'oiseau de bon augure', 'La tanière',
'Le détective créatif', 'Le détenteur originem', 'Le joker masqué', 'L\'équivalent de Batman',
'La folie téméraire', 'L\'aventurier au bon goût', 'L\'albatros invasif', 'Le mystère autonome',
'L\'origami impénétrable', 'Le forban adéquat', 'Le chaînon manquant', 'L\'anthropologue indécent', 'La terreur',
'Le dieu parmi les dieux','L\'anihilateur', 'Le diable', 'La goule', 'L\'élu', 'Le clochard']

        self.right_part = [['XSS', 0], ['injection SQL', 0], ['upload de backdoor', 1], ['crackme', 1], ['http splitting', 1],
['LOIC', 1], ['DoS', 1], ['Man in the Middle', 1], ['ARP spoofing', 0], ['Buffer Overflow', 1],
['RCE', 0], ['reverse', 1], ['OSINT', 0], ['forensics', 1], ['pwn', 1], ['stéganographie', 0],
['chiffre de césar', 1], ['double ROT 13', 1], ['injection d\'iframe', 0], ['logout CSRF', 0],
['Local File Include', 0], ['Remote File Include', 0], ['Google Dork', 1], ['Data leak', 1], ['CVE', 0],
['0day', 0], ['XXE', 0], ['malware', 1], ['cryptolocker', 1], ['wanacry', 1], ['heartbleed', 1],
['exploit', 1], ['nmap', 1], ['directory traversal', 1], ['race condition', 0], ['hash length extension attack', 0],
['attaque de Coppersmith', 0], ['obfuscation', 0], ['exécution spéculative', 0], ['self-XSS', 0], ['one-time pad', 1],
['ransomware JavaScript', 1], ['deface', 1], ['bruteforce', 1], ['troll', 1], ['épreuves de logique sur newbiecontest', 2],
['stack clash', 1], ['fastbin', 1], ['heap exploitation', 0], ['lecture de manuel', 0], ['exfiltration de données', 0],
['nanomites', 0], ['shellcodes alphanumériques', 2], ['Burp', 1], ['Wireshark', 1], ['FUD RAT', 1], ['botnets', 2],
['bypass mod_security', 1], ['fork bomb', 0], ['shellshock', 1], ['phishing', 1], ['scam 419', 1], ['XSS filter bypass', 1],
['injection SQL à l\'aveugle', 0], ['side-channel attack', 1], ['Linear-feedback shift register', 1],
['Return Oriented Programming', 1], ['Volatility', 1], ['format PDF', 1], ['charset GBK', 1],
['librairie base64 en python', 0], ['GAME', 1], ['vuln Java', 0], ['TOCTOU', 1], ['processeur 6502', 1],
['VM Hackthebox', 0], ['Vulnérabilités kernel', 2], ['déterrage de topic sur RSA', 1], ['opcode HCF', 1],
['communauté SNMP \'public\'', 0], ['communauté hack-free', 0], ['clé WEP', 0], ['cassage de wifi publics', 1], ['OpSec', 0]
        ]

    def calculate(self, pseudo):
        hashed = hashlib.md5(pseudo.encode('utf-8')).hexdigest()
        return (int(hashed[0:16], 16), int(hashed[16:], 16))


    def execute(self, **kwargs):
        datas = kwargs['datas']

        content = datas['content'].split(' ')
        pseudo = datas['from'] if len(content) == 1 else content[1]
        pseudo = pseudo[1:] if pseudo[0] == '@' else pseudo # specific for the discord<>irc bot https://github.com/Hackndo/discord-irc-sync
        hashed = self.calculate(pseudo)
        calculated_left = hashed[0]%len(self.left_part)
        calculated_right = hashed[1]%len(self.right_part)
        left = self.left_part[calculated_left]
        right = self.right_part[calculated_right][0]
        gender = self.right_part[calculated_right][1]
        middle = ' des ' if gender is 2 else ' de l\'' if right[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y'] else' du ' if gender is 1  else ' de la '

        self.rawSend('PRIVMSG', pseudo+' : '+left+middle+right, datas['to'])
