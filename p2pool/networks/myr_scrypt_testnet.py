from p2pool.bitcoin import networks


PARENT = networks.nets['myr_scrypt_testnet']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 12*60*60//20 # shares
REAL_CHAIN_LENGTH = 12*60*60//20 # shares
TARGET_LOOKBEHIND = 10 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'ef00aa11ee66aabb'.decode('hex')
PREFIX = '33ffaa1100bbaa11'.decode('hex')
P2P_PORT = 5555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5556
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-testnet'
VERSION_CHECK = lambda v: v >= 90206
