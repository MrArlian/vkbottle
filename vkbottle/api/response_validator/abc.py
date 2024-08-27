from abc import ABC, abstractmethod
from typing import Any

from vkbottle.api.abc import ABCAPI


class ABCResponseValidator(ABC):
    """Abstract Response Validator class
    Documentation: https://vkbottle.rtfd.io/ru/latest/low-level/api/response-validator
    """

    @abstractmethod
    async def validate(
        self, ctx_api: ABCAPI, method: str, data: dict, response: Any
    ) -> Any:
        pass
