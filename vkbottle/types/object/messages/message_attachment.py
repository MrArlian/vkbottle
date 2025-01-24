from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import MessagesMessageAttachmentType

from ...base import VkObject

if TYPE_CHECKING:
    from ..gifts.layout import Layout
    from ..video.video_full import VideoFull
    from ..wall.wall_comment import WallComment
    from ..docs.doc import Doc
    from ..photos.photo import Photo
    from ..base_sticker_new import BaseStickerNew
    from ..audio_audio import AudioAudio
    from ..base_link import BaseLink
    from ..wall.wallpost_full import WallpostFull


class MessageAttachment(VkObject):
    """VK Object MessagesMessageAttachment"""

    type: MessagesMessageAttachmentType
    audio: Optional[AudioAudio] = None
    doc: Optional[Doc] = None
    gift: Optional[Layout] = None
    photo: Optional[Photo] = None
    sticker: Optional[BaseStickerNew] = None
    video: Optional[VideoFull] = None
    link: Optional[BaseLink] = None
    wall_reply: Optional[WallComment] = None
    wall: Optional[WallpostFull] = None
