from typing import Tuple
from typing import Union
from typing import Callable
from ubelt.util_const import NoParamType
from typing import List
from os import PathLike
from _typeshed import Incomplete
from typing import TypeVar

Hasher = TypeVar("Hasher")
HASH_VERSION: int
DEFAULT_ALPHABET: Incomplete


def b(s):
    ...


DEFAULT_HASHER: Incomplete


class _Hashers:
    algos: Incomplete
    aliases: Incomplete

    def __init__(self) -> None:
        ...

    def available(self):
        ...

    def __contains__(self, key):
        ...

    def lookup(self, hasher):
        ...


class HashableExtensions:
    keyed_extensions: Incomplete
    iterable_checks: Incomplete

    def __init__(self) -> None:
        ...

    def register(self, hash_types: Union[type, Tuple[type]]) -> Callable:
        ...

    def lookup(self, data):
        ...

    def add_iterable_check(self, func):
        ...


class _HashTracer:
    sequence: Incomplete

    def __init__(self) -> None:
        ...

    def update(self, bytes) -> None:
        ...

    def hexdigest(self):
        ...


def hash_data(data: object,
              hasher: Union[str, Hasher, NoParamType] = ...,
              base: Union[List[str], str, NoParamType] = ...,
              types: bool = ...,
              convert: bool = ...,
              extensions: HashableExtensions = ...) -> str:
    ...


def hash_file(fpath: PathLike,
              blocksize: int = ...,
              stride: int = ...,
              maxbytes: Union[int, None] = ...,
              hasher: Union[str, Hasher, NoParamType] = ...,
              base: Union[List[str], str, NoParamType] = ...):
    ...
