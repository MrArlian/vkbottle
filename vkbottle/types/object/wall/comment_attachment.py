from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import WallCommentAttachmentType

from ...base import VkObject

if TYPE_CHECKING:
    from ..video.video import Video
    from .attached_note import AttachedNote
    from ..docs.doc import Doc
    from ..photos.photo import Photo
    from ..base_link import BaseLink
    from ..market.market_album import MarketAlbum
    from ..base_sticker_new import BaseStickerNew
    from ..market.market_item import MarketItem
    from ..audio_audio import AudioAudio
    from ..pages.wikipage_full import WikipageFull


class CommentAttachment(VkObject):
    """VK Object WallCommentAttachment"""

    audio: Optional[AudioAudio] = None
    doc: Optional[Doc] = None
    link: Optional[BaseLink] = None
    market: Optional[MarketItem] = None
    market_market_album: Optional[MarketAlbum] = None
    note: Optional[AttachedNote] = None
    page: Optional[WikipageFull] = None
    photo: Optional[Photo] = None
    sticker: Optional[BaseStickerNew] = None
    type: WallCommentAttachmentType
    video: Optional[Video] = None
