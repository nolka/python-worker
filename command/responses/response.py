from ..command import Configurable


class BaseResponse(Configurable):
    __slots__ = ('uuid', 'code',)
