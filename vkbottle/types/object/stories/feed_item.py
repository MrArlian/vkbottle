from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import FeedItemType

from ...base import VkObject

if TYPE_CHECKING:
    from .story import Story
    from .feed_item import FeedItem
    from .promo_block import PromoBlock
    from ..apps.app_min import AppMin


class FeedItem(VkObject):
    """VK Object StoriesFeedItem

    app - App, which stories has been grouped (for type app_grouped_stories)
    birthday_user_id -
    grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
    has_unseen -
    id -
    name -
    promo_data - Additional data for promo stories (for type promo_stories)
    stories - Author stories
    track_code -
    type - Type of Feed Item
    """

    app: Optional[AppMin] = None
    birthday_user_id: Optional[int] = None
    grouped: Optional[List[FeedItem]] = None
    has_unseen: Optional[bool] = None
    id: Optional[str] = None
    name: Optional[str] = None
    promo_data: Optional[PromoBlock] = None
    stories: Optional[List[Story]] = None
    track_code: Optional[str] = None
    type: FeedItemType
