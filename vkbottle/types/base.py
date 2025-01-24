from typing import Optional, Any

from pydantic import BaseModel, PrivateAttr

from vkbottle.api.abc import ABCAPI


class BotApiContext(BaseModel):
    _api: Optional[ABCAPI] = PrivateAttr()

    def __init__(
        self,
        ctx_api: Optional[ABCAPI] = None,
        **data: Any
    ) -> None:
        self._api = ctx_api
        super().__init__(**data)

    @property
    def api(self) -> Optional[ABCAPI]:
        """
            ...
        """
        return self._api


class VkObject(BotApiContext, BaseModel):

    class Config:
        frozen = True
