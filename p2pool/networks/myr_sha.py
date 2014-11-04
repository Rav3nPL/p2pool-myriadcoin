from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myr_sha']
SHARE_PERIOD = 10 # seconds
NEW_SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 50 # shares //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 30 # blocks
NEW_SPREAD = 30 # blocks
IDENTIFIER = 'fc70135c700a00ee'.decode('hex')
PREFIX = '9472ef181e88efcb'.decode('hex')
P2P_PORT = 5577
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5578
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org nz.p2pool.geek.nz'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: v >= 90206
