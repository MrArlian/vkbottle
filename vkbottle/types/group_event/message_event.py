from __future__ import annotations

import logging
import json

from typing import TYPE_CHECKING, Callable, Optional, Union, Dict, List, Any
from io import StringIO

from ..base import VkObject

if TYPE_CHECKING:
    from vkbottle_types.responses.messages import MessagesSendUserIdsResponseItem
    from ..object.messages.forward import Forward


class MessageEvent(VkObject):
    user_id: int
    peer_id: int
    event_id: str
    payload: Optional[Dict[str, Any]] = None
    conversation_message_id: Optional[int] = None

    @property
    def from_id(self) -> int:
        return self.user_id

    def get_payload_json(
        self,
        throw_error: bool = False,
        unpack_failure: Callable[..., Any] = lambda payload: payload,
    ) -> Optional[Union[Dict[str, Any], Any]]:
        """
            ...
        """
        if self.payload is None:
            return
        if isinstance(self.payload, dict):
            return self.payload.copy()
        try:
            return json.loads(self.payload)
        except (ValueError, TypeError) as e:
            if throw_error:
                raise e from e
        return unpack_failure(self.payload)

    async def answer(self, text: str) -> int:
        event_data = {
            'type': 'show_snackbar',  'text': text
        }
        return await self.api.messages.send_message_event_answer(
            event_id=self.event_id,
            user_id=self.from_id,
            peer_id=self.peer_id,
            event_data=json.dumps(event_data)
        )

    async def message_edit(
        self,
        message: Optional[str] = None,
        attachment: Optional[str] = None,
        random_id: Optional[int] = 0,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        reply_to: Optional[int] = None,
        forward_messages: Optional[List[int]] = None,
        forward: Optional[str] = None,
        sticker_id: Optional[int] = None,
        keyboard: Optional[str] = None,
        template: Optional[str] = None,
        payload: Optional[str] = None,
        content_source: Optional[str] = None,
        dont_parse_links: Optional[bool] = None,
        disable_mentions: Optional[bool] = None,
        intent: Optional[str] = None,
        subscribe_id: Optional[int] = None,
        **kwargs,
    ) -> bool:
        locals().update(kwargs)

        deprecated_params = (
            "self", "kwargs", "peer_id", "user_id", "domain",
            "chat_id", "user_ids", "conversation_message_id", "message"
        )
        data = {
            k: v for k, v in locals().items()
            if k not in deprecated_params and v is not None
        }

        if message is None:
            message = ""
        if not isinstance(message, str):
            message = str(message)

        return await self.api.messages.edit(
            peer_id=self.peer_id,
            conversation_message_id=self.conversation_message_id,
            message=message,
            **data
        )

    async def new_message_send(
        self,
        message: Optional[str] = None,
        attachment: Optional[str] = None,
        random_id: Optional[int] = 0,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        reply_to: Optional[int] = None,
        forward_messages: Optional[List[int]] = None,
        forward: Optional[str] = None,
        sticker_id: Optional[int] = None,
        keyboard: Optional[str] = None,
        template: Optional[str] = None,
        payload: Optional[str] = None,
        content_source: Optional[str] = None,
        dont_parse_links: Optional[bool] = None,
        disable_mentions: Optional[bool] = None,
        intent: Optional[str] = None,
        subscribe_id: Optional[int] = None,
        **kwargs,
    ) -> MessagesSendUserIdsResponseItem:
        locals().update(kwargs)

        data = {k: v for k, v in locals().items() if k not in ("self", "kwargs") and v is not None}
        deprecated_params = ("peer_id", "user_id", "domain", "chat_id", "user_ids")
        deprecated = [k for k in data if k in deprecated_params]
        if deprecated:
            logging.warning(
                "Params like peer_id or user_id is deprecated in Message.answer()."
                "Use API.messages.send() instead"
            )
            for k in deprecated:
                data.pop(k)
        if message is None:
            message = ""
        elif not isinstance(message, str):
            message = str(message)
        stream = StringIO(message)
        while True:
            msg = stream.read(4096)
            if msg:
                data["message"] = msg
            response = (await self.api.messages.send(peer_ids=[self.peer_id], **data))[0]
            if stream.tell() == len(message or ""):
                break
        return response

    async def reply(
        self,
        message: Optional[str] = None,
        attachment: Optional[str] = None,
        **kwargs,
    ) -> MessagesSendUserIdsResponseItem:
        locals().update(kwargs)

        data = {k: v for k, v in locals().items() if k not in ("self", "kwargs") and v is not None}
        data["forward"] = Forward(
            conversation_message_ids=[self.conversation_message_id],
            peer_id=self.peer_id,
            is_reply=True,
        ).json()

        return await self.new_message_send(**data)

    async def forward(
        self,
        message: Optional[str] = None,
        attachment: Optional[str] = None,
        **kwargs,
    ) -> MessagesSendUserIdsResponseItem:
        locals().update(kwargs)

        data = {
            k: v
            for k, v in locals().items()
            if k not in ("self", "kwargs", "forward_message_ids") and v is not None
        }
        data["forward"] = Forward(
            conversation_message_ids=[self.conversation_message_id],
            peer_id=self.peer_id
        ).json()

        return await self.new_message_send(**data)
