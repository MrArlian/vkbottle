from typing import Callable, Awaitable, Dict, Any
from abc import ABC, abstractmethod

from vkbottle.types.base import VkObject


MiddlewareHandlerType = Callable[[VkObject, Dict[str, Any]], Awaitable[Any]]


class BaseMiddleware(ABC):

    @abstractmethod
    async def __call__(
        self,
        handler: MiddlewareHandlerType,
        event: VkObject,
        context: Dict[str, Any]
    ) -> Any:
        """
            ...
        """
