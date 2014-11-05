from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myr_skein_testnet']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 10
SPREAD = 30
IDENTIFIER = 'ee87aa00bb11ffee'.decode('hex')
PREFIX = 'a0bb1166eeff77aa'.decode('hex')
P2P_PORT = 5588
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5589
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-testnet'
VERSION_CHECK = lambda v: v >= 90206
