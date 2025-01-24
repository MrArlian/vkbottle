from __future__ import annotations

from ...base import VkObject


class PromoBlock(VkObject):
    """VK Object StoriesPromoBlock

    name - Promo story title
    not_animated - Hide animation for promo story
    photo_100 - RL of square photo of the story with 100 pixels in width
    photo_50 - RL of square photo of the story with 50 pixels in width
    """

    name: str
    not_animated: bool
    photo_100: str
    photo_50: str
