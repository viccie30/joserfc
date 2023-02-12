from abc import ABCMeta, abstractmethod


class JWSAlgorithm(object, metaclass=ABCMeta):
    """Interface for JWS algorithm. JWA specification (RFC7518) SHOULD
    implement the algorithms for JWS with this base implementation.
    """
    name = None
    description = None
    location = 'alg'

    @abstractmethod
    def sign(self, msg: bytes, key) -> bytes:
        """Sign the text msg with a private/sign key.

        :param msg: message bytes to be signed
        :param key: private key to sign the message
        :return: bytes
        """
        pass

    @abstractmethod
    def verify(self, msg: bytes, sig: bytes, key) -> bool:
        """Verify the signature of text msg with a public/verify key.

        :param msg: message bytes to be signed
        :param sig: result signature to be compared
        :param key: public key to verify the signature
        :return: boolean
        """
        pass