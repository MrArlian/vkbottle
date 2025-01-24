from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .rules import Rules


class RejectReason(VkObject):
    """VK Object AdsRejectReason

    comment - Comment text
    rules -
    """

    comment: Optional[str] = None
    rules: Optional[List[Rules]] = None
