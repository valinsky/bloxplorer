from types import SimpleNamespace

BITCOIN_API_BASE_URL = 'https://blockstream.info/api/'
BITCOIN_TESTNET_API_BASE_URL = 'https://blockstream.info/testnet/api/'
BITCOIN_SIGNET_API_BASE_URL = 'https://blockstream.info/signet/api/'
LIQUID_API_BASE_URL = 'https://blockstream.info/liquid/api/'

DEFAULT_TIMEOUT = 5
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_TEXT = 'text/plain'

P2PKH = 'P2PKH'
P2SH = 'P2SH'
BECH32 = 'BECH32'
BIP32_PUBKEY = 'BIP32 Public Key'
BIP32_PRVKEY = 'BIP32 Pivate Key'
UNRECOGNIZED_ADDRESS_TYPE = 'Unrecognized address type'

REQUEST_TIMED_OUT_MESSAGE = 'Request timed out.'
NETWORK_ERROR_MESSAGE = 'Network error.'
INVALID_API_RESOURCE_MESSAGE = 'Invalid API resource.'
UNKNOWN_ERROR_MESSAGE = 'An unknown error occured while processing your request.'

http = SimpleNamespace(
    GET='GET',
    POST='POST'
)
