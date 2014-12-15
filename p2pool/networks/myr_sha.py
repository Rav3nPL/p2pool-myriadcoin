from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myr_sha']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 10 # shares //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 30 # blocks
IDENTIFIER = 'ef0022a7f188e6ba'.decode('hex')
PREFIX = 'b1a622f061a7eb1a'.decode('hex')
P2P_PORT = 5577
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 5578
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org aforis.mooo.com p2poolcoin.com us.myriadminers.com eu.myriadminers.com nz.p2pool.geek.nz rav3n.dtdns.net p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: v >= 90206
