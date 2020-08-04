from p2pool.qnodecoin import networks

PARENT = networks.nets['qnodecoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
#IDENTIFIER = '7242ef345e1bed6b'.decode('hex')
IDENTIFIER = '7242ef648e1bed6b'.decode('hex')
#PREFIX =  '3b3e1286f446b891'.decode('hex')
PREFIX = '3b3e1257f446b891'.decode('hex')
COINBASEEXT =  '0D2F5032506F6F6C2D514E4F4445434F494E2F'.decode('hex')
P2P_PORT = 20612
MIN_TARGET = 0
MAX_TARGET = 2**256//2**30 - 1
PERSIST = False
WORKER_PORT = 8500

#BOOTSTRAP_ADDRS = 'qnodecoin01.p2poolmining.us p2pool.2sar.ru qnodecoin02.p2poolmining.us p2pool.qnodecoin.siampm.com qnodecoin03.p2poolmining.us crypto.office-on-the.net qnodecoin04.p2poolmining.us'.split(' ')

BOOTSTRAP_ADDRS = '140.82.9.137 154.223.134.122 47.245.0.245 45.76.211.195 110.232.115.241 174.138.33.59 149.28.59.152'.split(' ')
#BOOTSTRAP_ADDRS = 'p2pool.2sar.ru crypto.office-on-the.net'.split(' ')
ANNOUNCE_CHANNEL = '#qnodecoin-p2pool'
VERSION_CHECK = lambda v: v >= 170200
