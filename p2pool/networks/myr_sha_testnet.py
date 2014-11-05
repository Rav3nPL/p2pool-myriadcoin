from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myr_sha_testnet']
SHARE_PERIOD = 30 # seconds
NEW_SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 10 # shares //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 30 # blocks
IDENTIFIER = 'ee0fee0faa2faa2f'.decode('hex')
PREFIX = 'aaff22cc33bb66aa'.decode('hex')
P2P_PORT = 5577
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5578
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-testnet'
VERSION_CHECK = lambda v: v >= 90206
