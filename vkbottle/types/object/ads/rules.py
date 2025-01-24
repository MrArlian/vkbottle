from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .paragraphs import Paragraphs


class Rules(VkObject):
    """VK Object AdsRules

    paragraphs -
    title - Comment
    """

    paragraphs: Optional[List[Paragraphs]] = None
    title: Optional[str] = None
