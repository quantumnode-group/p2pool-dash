import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'bf0c6bbd'.decode('hex')
P2P_PORT = 20612
ADDRESS_VERSION = 76
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 20611
RPC_CHECK = defer.inlineCallbacks(lambda qnodecoind: defer.returnValue(
            (yield helper.check_block_header(qnodecoind, '00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6')) and
            (yield qnodecoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('qnodecoin_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('qnodecoin_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'QNODECOIN'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'QnodecoinCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/QnodecoinCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.qnodecoin'), 'qnodecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/qnodecoin/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/qnodecoin/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/qnodecoin/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
