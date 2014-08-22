from p2pool.bitcoin import networks

PARENT = networks.nets['guldencoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'fc6562888326696e'.decode('hex')
PREFIX = 'fe63ededfe6c888a'.decode('hex')
P2P_PORT = 27000
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 27100
BOOTSTRAP_ADDRS = 'dutchpool.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
