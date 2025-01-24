from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import MessagesHistoryMessageAttachmentType

from ...base import VkObject

if TYPE_CHECKING:
    from ..video.video import Video
    from .graffiti import Graffiti
    from ..docs.doc import Doc
    from ..photos.photo import Photo
    from ..base_link import BaseLink
    from ..market.market_item import MarketItem
    from ..audio_audio import AudioAudio
    from ..wall.wallpost_full import WallpostFull
    from .audio_message import AudioMessage


class HistoryMessageAttachment(VkObject):
    """VK Object MessagesHistoryMessageAttachment"""

    audio: Optional[AudioAudio] = None
    audio_message: Optional[AudioMessage] = None
    doc: Optional[Doc] = None
    graffiti: Optional[Graffiti] = None
    link: Optional[BaseLink] = None
    market: Optional[MarketItem] = None
    photo: Optional[Photo] = None
    type: MessagesHistoryMessageAttachmentType
    video: Optional[Video] = None
    wall: Optional[WallpostFull] = None
