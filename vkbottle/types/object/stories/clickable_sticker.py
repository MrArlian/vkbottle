from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import (
    StoriesClickableStickerSubtype,
    StoriesClickableStickerType,
    StoriesClickableStickerStyle
)

from ...base import VkObject

if TYPE_CHECKING:
    from .clickable_area import ClickableArea
    from ..apps.app_min import AppMin
    from ..base_link import BaseLink
    from ..market.market_item import MarketItem
    from ..audio_audio import AudioAudio
    from ..polls.poll import Poll


class ClickableSticker(VkObject):
    """VK Object StoriesClickableSticker

    app -
    app_context - Additional context for app sticker
    audio -
    audio_start_time -
    clickable_area -
    color - Color, hex format
    has_new_interactions - Whether current user has unread interaction with this app
    hashtag -
    id - Clickable sticker ID
    is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
    link_object -
    market_item -
    mention -
    owner_id -
    place_id -
    poll -
    post_id -
    post_owner_id -
    question -
    question_button -
    situational_app_url -
    situational_theme_id -
    sticker_id - Sticker ID
    sticker_pack_id - Sticker pack ID
    story_id -
    style -
    subtype -
    tooltip_text -
    type -
    """

    app: Optional[AppMin] = None
    app_context: Optional[str] = None
    audio: Optional[AudioAudio] = None
    audio_start_time: Optional[int] = None
    clickable_area: List[ClickableArea]
    color: Optional[str] = None
    has_new_interactions: Optional[bool] = None
    hashtag: Optional[str] = None
    id: int
    is_broadcast_notify_allowed: Optional[bool] = None
    link_object: Optional[BaseLink] = None
    market_item: Optional[MarketItem] = None
    mention: Optional[str] = None
    owner_id: Optional[int] = None
    place_id: Optional[int] = None
    poll: Optional[Poll] = None
    post_id: Optional[int] = None
    post_owner_id: Optional[int] = None
    question: Optional[str] = None
    question_button: Optional[str] = None
    situational_app_url: Optional[str] = None
    situational_theme_id: Optional[int] = None
    sticker_id: Optional[int] = None
    sticker_pack_id: Optional[int] = None
    story_id: Optional[int] = None
    style: Optional[StoriesClickableStickerStyle] = None
    subtype: Optional[StoriesClickableStickerSubtype] = None
    tooltip_text: Optional[str] = None
    type: StoriesClickableStickerType
