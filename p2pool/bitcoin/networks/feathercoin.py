import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 9336
ADDRESS_VERSION = 14
RPC_PORT = 9337
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'feathercoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 200*100000000 >> (height + 1)//3360000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'FTC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.feathercoin'), 'feathercoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://cryptocoinexplorer.com:5750/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://cryptocoinexplorer.com:5750/address/'
TX_EXPLORER_URL_PREFIX = 'http://cryptocoinexplorer.com:5750/transaction/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8