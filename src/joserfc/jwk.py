from typing import Union
from .rfc7517.keys import SymmetricKey, AsymmetricKey, Key
from .rfc7518.oct_key import OctKey
from .rfc7518.rsa_key import RSAKey
from .rfc7518.ec_key import ECKey


__all__ = [
    'SymmetricKey',
    'AsymmetricKey',
    'Key',
    'OctKey',
    'RSAKey',
    'ECKey',
    'JWK_REGISTRY',
    'generate_key',
]


JWK_REGISTRY = {
    OctKey.key_type: OctKey,
    RSAKey.key_type: RSAKey,
    ECKey.key_type: ECKey,
}


def generate_key(key_type: str, crv_or_size: Union[str, int], options=None, private=False):
    pass
