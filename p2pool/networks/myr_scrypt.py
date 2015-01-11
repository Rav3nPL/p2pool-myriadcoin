from p2pool.bitcoin import networks


PARENT = networks.nets['myr_scrypt']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 12*60*60//20 # shares
REAL_CHAIN_LENGTH = 12*60*60//20 # shares
TARGET_LOOKBEHIND = 10 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'e0b1882a8e10fab6'.decode('hex')
PREFIX = 'a7f1b3881a02ee81'.decode('hex')
P2P_PORT = 5555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5556
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org aforis.mooo.com p2poolcoin.com us.myriadminers.com eu.myriadminers.com nz.p2pool.geek.nz rav3n.dtdns.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: v >= 90206
