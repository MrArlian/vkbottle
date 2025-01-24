from typing import Any, Sequence, Union, Dict

from vkbottle.types import (
    MessageNew,
    MessageReply,
    MessageEdit,
    MessageEvent,
    VkObject
)

from .base import BaseRule


VkMessageTypes = (
    MessageNew,
    MessageEdit,
    MessageReply,
    MessageEvent
)


class RawPayloadRule(BaseRule):

    def __init__(
        self,
        payload: Union[Sequence[Dict[str, Any]], Dict[str, Any]]
    ) -> None:
        if not isinstance(payload, (list, tuple, set)):
            payload = (payload,)
        self.payload = payload

    async def __call__(self, event: VkObject, **kwargs: Any) -> bool:
        if not isinstance(event, VkMessageTypes):
            return False
        return event.get_payload_json() in self.payload
