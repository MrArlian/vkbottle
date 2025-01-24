from typing import List, Union, SupportsIndex, Any, Dict, overload
from functools import wraps, partial

from vkbottle.types import VkObject

from ..handler import CallbackType
from .base import BaseMiddleware


class MiddlewareManager:

    def __init__(self) -> None:
        self._middlewares: List[BaseMiddleware] = []

    def register(self, middleware: BaseMiddleware) -> None:
        if not isinstance(middleware, BaseMiddleware):
            raise TypeError(
                f"Expected instance of BaseMiddleware, got {type(middleware).__name__}"
            )
        self._middlewares.append(middleware)

    def wrap_middlewares(self, callback: CallbackType) -> CallbackType:
        """
            ...
        """
        @wraps(callback)
        def _wrapper(event: VkObject, context: Dict[str, Any]) -> Any:
            return callback(event, **context)

        _middleware = _wrapper
        for middleware in reversed(self._middlewares):
            _middleware = partial(middleware, _middleware)
        return _middleware

    def apply_middlewares(
        self,
        callback: CallbackType,
        event: VkObject,
        context: Dict[str, Any]
    ) -> Any:
        """
            ...
        """
        _wrapper = self.wrap_middlewares(callback)
        return _wrapper(event, context)

    def __call__(self, middleware: BaseMiddleware) -> None:
        self.register(middleware)

    @overload
    def __getitem__(self, item: SupportsIndex) -> BaseMiddleware:
        pass

    @overload
    def __getitem__(self, item: slice) -> List[BaseMiddleware]:
        pass

    def __getitem__(self, item) -> Union[BaseMiddleware, List[BaseMiddleware]]:
        return self._middlewares[item]

    def __len__(self) -> int:
        return len(self._middlewares)
