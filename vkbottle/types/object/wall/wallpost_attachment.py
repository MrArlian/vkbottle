from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import WallWallpostAttachmentType

from ...base import VkObject

if TYPE_CHECKING:
    from ..events_event_attach import EventsEventAttach
    from ..video.video_full import VideoFull
    from .posted_photo import PostedPhoto
    from ..notes.note import Note
    from .graffiti import Graffiti
    from ..market.market_item import MarketItem
    from ..docs.doc import Doc
    from ..photos.photo import Photo
    from .app_post import AppPost
    from ..base_link import BaseLink
    from ..market.market_album import MarketAlbum
    from ..groups.group_attach import GroupAttach
    from ..audio_audio import AudioAudio
    from ..polls.poll import Poll
    from ..photos.photo_album import PhotoAlbum
    from ..pages.wikipage_full import WikipageFull


class WallpostAttachment(VkObject):
    """VK Object WallWallpostAttachment

    access_key - Access key for the audio
    album -
    app -
    audio -
    doc -
    event -
    graffiti -
    group -
    link -
    market -
    market_album -
    note -
    page -
    photo -
    poll -
    posted_photo -
    type -
    video -
    """

    access_key: Optional[str] = None
    album: Optional[PhotoAlbum] = None
    app: Optional[AppPost] = None
    audio: Optional[AudioAudio] = None
    doc: Optional[Doc] = None
    event: Optional[EventsEventAttach] = None
    graffiti: Optional[Graffiti] = None
    group: Optional[GroupAttach] = None
    link: Optional[BaseLink] = None
    market: Optional[MarketItem] = None
    market_album: Optional[MarketAlbum] = None
    note: Optional[Note] = None
    page: Optional[WikipageFull] = None
    photo: Optional[Photo] = None
    poll: Optional[Poll] = None
    posted_photo: Optional[PostedPhoto] = None
    type: WallWallpostAttachmentType
    video: Optional[VideoFull] = None
