from __future__ import annotations

import logging
import json

from typing import TYPE_CHECKING, Callable, List, Optional, Union, Dict, Any
from io import StringIO

from pydantic import Field

from ..object.messages import Message
from ..object.client_info_for_bots import ClientInfoForBots
from ..object.users import UserFull

if TYPE_CHECKING:
    from vkbottle_types.responses.messages import MessagesSendUserIdsResponseItem

    from ..object.gifts.layout import Layout
    from ..object.video.video_full import VideoFull
    from ..object.wall.wall_comment import WallComment
    from ..object.docs.doc import Doc
    from ..object.photos.photo import Photo
    from ..object.base_sticker_new import BaseStickerNew
    from ..object.audio_audio import AudioAudio
    from ..object.base_link import BaseLink
    from ..object.wall.wallpost_full import WallpostFull
    from ..object.messages.forward import Forward


from ..base import VkObject


class MessageNew(VkObject):
    full_message: Message = Field(alias='message')
    client_info: ClientInfoForBots

    @property
    def message_id(self) -> int:
        return (
            self.full_message.conversation_message_id or
            self.full_message.id
        )

    @property
    def chat_id(self) -> int:
        return self.full_message.peer_id - 2_000_000_000

    @property
    def from_id(self) -> int:
        return self.full_message.from_id

    @property
    def text(self) -> str:
        return self.full_message.text

    @property
    def payload(self) -> Optional[str]:
        return self.full_message.payload

    @property
    def audio_attachments(self) -> List[AudioAudio]:
        return [i.audio for i in self.full_message.attachments if i.audio]

    @property
    def doc_attachments(self) -> List[Doc]:
        return [i.doc for i in self.full_message.attachments if i.doc]

    @property
    def gift_attachments(self) -> List[Layout]:
        return [i.gift for i in self.full_message.attachments if i.gift]

    @property
    def photo_attachments(self) -> List[Photo]:
        return [i.photo for i in self.full_message.attachments if i.photo]

    @property
    def sticker_attachments(self) -> List[BaseStickerNew]:
        return [i.sticker for i in self.full_message.attachments if i.sticker]

    @property
    def video_attachments(self) -> List[VideoFull]:
        return [i.video for i in self.full_message.attachments if i.video]

    @property
    def link_attachments(self) -> List[BaseLink]:
        return [i.link for i in self.full_message.attachments if i.link]

    @property
    def wall_reply_attachments(self) -> List[WallComment]:
        return [i.wall_reply for i in self.full_message.attachments if i.wall_reply]

    @property
    def wall_attachments(self) -> List[WallpostFull]:
        return [i.wall for i in self.full_message.attachments if i.wall]

    def get_payload_json(
        self,
        throw_error: bool = False,
        unpack_failure: Callable[..., Any] = lambda payload: payload,
    ) -> Optional[Union[Dict[str, Any], Any]]:
        """
            ...
        """
        if self.full_message.payload is None:
            return
        try:
            return json.loads(self.full_message.payload)
        except (ValueError, TypeError) as e:
            if throw_error:
                raise e from e
        return unpack_failure(self.full_message.payload)

    async def get_user(self, **kwargs: Any) -> UserFull:
        """
            ...
        """
        kwargs.update(user_ids=self.full_message.from_id)
        full_users = await self.api.request("users.get", kwargs)
        return UserFull(**full_users['response'][0])

    async def answer(
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
            response = (await self.api.messages.send(peer_ids=[self.full_message.peer_id], **data))[0]
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
            conversation_message_ids=[self.full_message.conversation_message_id],
            peer_id=self.full_message.peer_id,
            is_reply=True,
        ).json()

        return await self.answer(**data)

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
            conversation_message_ids=[self.full_message.conversation_message_id],
            peer_id=self.full_message.peer_id
        ).json()

        return await self.answer(**data)
