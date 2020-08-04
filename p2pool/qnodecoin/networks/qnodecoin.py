import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'a0dfbfdc'.decode('hex')
P2P_PORT = 20612
ADDRESS_VERSION = 20
SCRIPT_ADDRESS_VERSION = 21
RPC_PORT = 20611
RPC_CHECK = defer.inlineCallbacks(lambda qnodecoind: defer.returnValue(
            (yield helper.check_block_header(qnodecoind, '00000802cb89aa05be73de7e91ae33aec597c41f2f3832a2a95a5202400e5718')) and
            (yield qnodecoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('qnodecoin_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('qnodecoin_hash').getPoWHash(data))
BLOCK_PERIOD = 300 # s
SYMBOL = 'QNC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Qnodecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Qnodecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.qnodecoin'), 'qnodecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.qngnode.cc/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.qngnode.cc/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.qngnode.cc/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
