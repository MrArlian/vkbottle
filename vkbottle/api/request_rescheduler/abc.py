from abc import ABC, abstractmethod
from typing import Any

from vkbottle.api.abc import ABCAPI


class ABCRequestRescheduler(ABC):

    @abstractmethod
    async def reschedule(
        self, ctx_api: ABCAPI, method: str, data: dict, response: Any
    ) -> Any:
        pass
