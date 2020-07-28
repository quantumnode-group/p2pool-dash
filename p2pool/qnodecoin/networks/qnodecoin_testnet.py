import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'cee2caff'.decode('hex')
P2P_PORT = 120612
ADDRESS_VERSION = 140
SCRIPT_ADDRESS_VERSION = 19
RPC_PORT = 120611
RPC_CHECK = defer.inlineCallbacks(lambda qnodecoind: defer.returnValue(
            (yield helper.check_block_header(qnodecoind, '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c')) and
            (yield qnodecoind.rpc_getblockchaininfo())['chain'] != 'main'
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('qnodecoin_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('qnodecoin_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tQNODECOIN'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'QnodecoinCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/QnodecoinCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.qnodecoin'), 'qnodecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://testnet-insight.qnodecoinevo.org/insight/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://testnet-insight.qnodecoinevo.org/insight/address/'
TX_EXPLORER_URL_PREFIX = 'https://testnet-insight.qnodecoinevo.org/insight/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**20 - 1)
DUST_THRESHOLD = 0.001e8
