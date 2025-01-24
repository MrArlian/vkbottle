from __future__ import annotations

from functools import wraps, partial

from typing import TYPE_CHECKING, List, Any, Dict, Sequence

from vkbottle.types.base import VkObject

from ..handler import HandlerObject, RuleObject, CallbackType
from ..middlewares.manager import MiddlewareManager
from ..middlewares.base import BaseMiddleware

if TYPE_CHECKING:
    from vkbottle.dispatch.router import BotRouter


HandlerNotFound = object()


def wrap_middlewares(
    middlewares: Sequence[BaseMiddleware],
    callback: CallbackType
) -> CallbackType:
    """
        ...
    """
    @wraps(callback)
    def _wrapper(event: VkObject, context: Dict[str, Any]) -> Any:
        return callback(event, **context)

    _middleware = _wrapper
    for middleware in reversed(middlewares):
        _middleware = partial(middleware, _middleware)
    return _middleware


class VkSingleEventManager:
    """
        ...
    """

    def __init__(self, *, router: BotRouter, event_name: str) -> None:
        self.router = router
        self.event_name = event_name

        self.handlers: List[HandlerObject] = []

        self.root_middleware = MiddlewareManager()
        self.middleware = MiddlewareManager()

    def _resolve_middlewares(self) -> List[BaseMiddleware]:
        middlewares: List[BaseMiddleware] = []

        for router in reversed(tuple(self.router.parent_chain)):
            if event := router.event_manager_map.get(self.event_name):
                middlewares.extend(event.middleware)

        return middlewares

    async def trigger(self, event: VkObject, **context: Any) -> Any:
        """
            ...
        """
        for handler_object in self.handlers:
            context["handler"] = handler_object
            result, data = await handler_object.rule_checking(event, **context)

            if result:
                context.update(data)

                # try:
                wrapper = wrap_middlewares(
                    middlewares=self._resolve_middlewares(),
                    callback=handler_object,
                )
                return await wrapper(event, context)
                # except Exception:
                #     continue

        return HandlerNotFound

    def add_handler(
        self,
        callback: CallbackType,
        *rules: CallbackType
    ) -> None:
        """
            ...
        """
        self.handlers.append(
            HandlerObject(
                callback=callback,
                rules=[RuleObject(i) for i in rules]
            )
        )

    def __call__(self, *rules: CallbackType) -> Any:
        """
            ...
        """
        def handler_wrap(handler: CallbackType) -> CallbackType:
            self.add_handler(handler, *rules)
            return handler
        return handler_wrap
