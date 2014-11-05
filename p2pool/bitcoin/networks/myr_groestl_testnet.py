import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '01f555a4'.decode('hex')
P2P_PORT = 20888
ADDRESS_VERSION = 88
RPC_PORT = 20889
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
		'myriadcoinaddress' in (yield bitcoind.rpc_help()) and
		(yield bitcoind.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 1000*100000000 >> (height + 1)//967680
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('groestl_hash').getPoWHash(data))
BLOCK_PERIOD = 30 #s
SYMBOL = 'MYR'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'myriadcoin') if platform.system() == 'Windows' 
			else os.path.expanduser('~/Library/Application Support/myriadcoin/') if platform.system() == 'Darwin' 
			else os.path.expanduser('~/.myriadcoin'), 'myriadcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://myr.theblockexplorer.com:2750/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://myr.theblockexplorer.com:2750/address/'
TX_EXPLORER_URL_PREFIX = 'http://myr.theblockexplorer.com:2750/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**27 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.0001
