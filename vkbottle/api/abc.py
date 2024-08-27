from abc import ABC, abstractmethod
from typing import Any, Self

from vkbottle_types.categories import APICategories


class ABCAPI(APICategories, ABC):

    @abstractmethod
    async def request(self, method: str, data: dict) -> dict:
        pass

    @abstractmethod
    async def validate_response(self, method: str, data: dict, response: Any) -> Any:
        pass

    @abstractmethod
    async def validate_request(self, request: Any) -> Any:
        pass

    @property
    def api_instance(self) -> Self:
        return self

    async def execute(self, code: str) -> Any:
        return await self.api_instance.request("execute", {"code": code})
