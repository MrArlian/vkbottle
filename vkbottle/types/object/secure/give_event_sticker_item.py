from __future__ import annotations

from typing import Optional

from ...base import VkObject


class GiveEventStickerItem(VkObject):
    """VK Object SecureGiveEventStickerItem"""

    status: Optional[str] = None
    user_id: Optional[int] = None
