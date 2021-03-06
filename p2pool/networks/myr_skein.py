from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myr_skein']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 20
SPREAD = 30
IDENTIFIER = 'e7f1aa882ab061e9'.decode('hex')
PREFIX = 'fb1a7ef520a175ec'.decode('hex')
P2P_PORT = 5588
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5589
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org aforis.mooo.com p2poolcoin.com us.myriadminers.com eu.myriadminers.com nz.p2pool.geek.nz rav3n.dtdns.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: v >= 90206
