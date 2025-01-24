from typing import Optional

from ..base import VkObject


class MarketCommentNew(VkObject):
    date: int
    from_id: int
    id: int
    market_owner_id: Optional[int] = None
    photo_id: Optional[int] = None
    text: Optional[str] = None
