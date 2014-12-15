import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'af4576ee'.decode('hex')
P2P_PORT = 10888
ADDRESS_VERSION = 50
RPC_PORT = 10889
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
		'myriadcoinaddress' in (yield bitcoind.rpc_help()) and
		not (yield bitcoind.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 1000*2000000000000 >> (height + 1)//967680
BLOCKHASH_FUNC = data.hash256
POW_FUNC = data.hash256
BLOCK_PERIOD = 30 # s
SYMBOL = 'MYR'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Myriadcoin') if platform.system() == 'Windows' 
		else os.path.expanuser('~/Library/Application Support/Myriadcoin/') if platform.system() == 'Darwin' 
		else os.path.expanduser('~/.myriadcoin'), 'myriadcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://myr.theblockexplorer.com:2750/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://myr.theblockexplorer.com:2750/address/'
TX_EXPLORER_URL_PREFIX = 'http://myr.theblockexplorer.com:2750/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.1
