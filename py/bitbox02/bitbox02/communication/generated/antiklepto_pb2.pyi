# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class AntiKleptoHostNonceCommitment(google___protobuf___message___Message):
    commitment = ... # type: bytes

    def __init__(self,
        *,
        commitment : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AntiKleptoHostNonceCommitment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"commitment"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"commitment",b"commitment"]) -> None: ...

class AntiKleptoSignerCommitment(google___protobuf___message___Message):
    commitment = ... # type: bytes

    def __init__(self,
        *,
        commitment : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AntiKleptoSignerCommitment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"commitment"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"commitment",b"commitment"]) -> None: ...

class AntiKleptoSignatureRequest(google___protobuf___message___Message):
    host_nonce = ... # type: bytes

    def __init__(self,
        *,
        host_nonce : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AntiKleptoSignatureRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"host_nonce"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"host_nonce",b"host_nonce"]) -> None: ...
